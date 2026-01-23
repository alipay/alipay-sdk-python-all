#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OcrAttachmentRes import OcrAttachmentRes


class AlipayCommerceMedicalOcrparsingUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalOcrparsingUploadResponse, self).__init__()
        self._attachment_list = None
        self._business_id = None
        self._business_type = None
        self._patient_id = None

    @property
    def attachment_list(self):
        return self._attachment_list

    @attachment_list.setter
    def attachment_list(self, value):
        if isinstance(value, list):
            self._attachment_list = list()
            for i in value:
                if isinstance(i, OcrAttachmentRes):
                    self._attachment_list.append(i)
                else:
                    self._attachment_list.append(OcrAttachmentRes.from_alipay_dict(i))
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalOcrparsingUploadResponse, self).parse_response_content(response_content)
        if 'attachment_list' in response:
            self.attachment_list = response['attachment_list']
        if 'business_id' in response:
            self.business_id = response['business_id']
        if 'business_type' in response:
            self.business_type = response['business_type']
        if 'patient_id' in response:
            self.patient_id = response['patient_id']
