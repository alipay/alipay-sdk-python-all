#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UpdatePartnerRequest import UpdatePartnerRequest


class AnttechOceanbaseObglobalPartnerModifyModel(object):

    def __init__(self):
        self._update_partner_request = None

    @property
    def update_partner_request(self):
        return self._update_partner_request

    @update_partner_request.setter
    def update_partner_request(self, value):
        if isinstance(value, UpdatePartnerRequest):
            self._update_partner_request = value
        else:
            self._update_partner_request = UpdatePartnerRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.update_partner_request:
            if hasattr(self.update_partner_request, 'to_alipay_dict'):
                params['update_partner_request'] = self.update_partner_request.to_alipay_dict()
            else:
                params['update_partner_request'] = self.update_partner_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalPartnerModifyModel()
        if 'update_partner_request' in d:
            o.update_partner_request = d['update_partner_request']
        return o


