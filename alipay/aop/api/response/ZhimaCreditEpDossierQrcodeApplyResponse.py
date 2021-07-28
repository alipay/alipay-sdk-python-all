#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpDossierQrcodeApplyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDossierQrcodeApplyResponse, self).__init__()
        self._dossier_path = None
        self._expiration_time = None
        self._qr_code = None

    @property
    def dossier_path(self):
        return self._dossier_path

    @dossier_path.setter
    def dossier_path(self, value):
        self._dossier_path = value
    @property
    def expiration_time(self):
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, value):
        self._expiration_time = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDossierQrcodeApplyResponse, self).parse_response_content(response_content)
        if 'dossier_path' in response:
            self.dossier_path = response['dossier_path']
        if 'expiration_time' in response:
            self.expiration_time = response['expiration_time']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
