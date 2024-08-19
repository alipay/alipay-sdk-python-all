#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MaterialUploadDetail import MaterialUploadDetail


class AlipayDataDataserviceAdMaterialQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdMaterialQueryResponse, self).__init__()
        self._material_upload_detail = None

    @property
    def material_upload_detail(self):
        return self._material_upload_detail

    @material_upload_detail.setter
    def material_upload_detail(self, value):
        if isinstance(value, MaterialUploadDetail):
            self._material_upload_detail = value
        else:
            self._material_upload_detail = MaterialUploadDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdMaterialQueryResponse, self).parse_response_content(response_content)
        if 'material_upload_detail' in response:
            self.material_upload_detail = response['material_upload_detail']
