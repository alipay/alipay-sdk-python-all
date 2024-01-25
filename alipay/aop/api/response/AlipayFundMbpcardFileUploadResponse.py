#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OcrData import OcrData


class AlipayFundMbpcardFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundMbpcardFileUploadResponse, self).__init__()
        self._image_id = None
        self._ocr_data = None

    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def ocr_data(self):
        return self._ocr_data

    @ocr_data.setter
    def ocr_data(self, value):
        if isinstance(value, list):
            self._ocr_data = list()
            for i in value:
                if isinstance(i, OcrData):
                    self._ocr_data.append(i)
                else:
                    self._ocr_data.append(OcrData.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundMbpcardFileUploadResponse, self).parse_response_content(response_content)
        if 'image_id' in response:
            self.image_id = response['image_id']
        if 'ocr_data' in response:
            self.ocr_data = response['ocr_data']
