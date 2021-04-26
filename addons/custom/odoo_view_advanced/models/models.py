# -*- coding: utf-8 -*-
import io
import base64
from odoo import models, fields, api, exceptions


class CustomItem(models.Model):
    _name = 'odoo_view_advanced.custom_item'

    name = fields.Char(string='Descripción')
    unit_price = fields.Char(string='Precio unitario')


# Los "TransientModel" no se almacenan en base de datos.
# Es Odoo el que gestiona el ciclo de vida de los "TransientModel"
class UploadFile(models.TransientModel):
    _name = 'odoo_view_advanced.upload_file'

    upload_file = fields.Binary(string="Subir fichero", required=True)
    file_name = fields.Char(string="Nombre del fichero")

    def import_file(self):
        if self.file_name:
            if '.csv' not in self.file_name:
                raise exceptions.ValidationError('El archivo debe ser un CSV')
            file = self.read_file_from_binary(self.upload_file)
            lines = file.split('\n')
            for line in lines:
                elements = line.split(';')
                if len(elements) > 1:
                    self.env['odoo_view_advanced.custom_item'].create({
                        'name': elements[0],
                        'unit_price': float(elements[1])
                    })

    def read_file_from_binary(self, file):
        try:
            with io.BytesIO(base64.b64decode(file)) as f:
                f.seek(0)
                return f.read().decode('UTF-8')
        except Exception as e:
            pritn(str(e))
            raise e
