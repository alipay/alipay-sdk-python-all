#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenVoucherBizDataDTO(object):

    def __init__(self):
        self._encrypt_phone = None
        self._pet_inst_id = None

    @property
    def encrypt_phone(self):
        return self._encrypt_phone

    @encrypt_phone.setter
    def encrypt_phone(self, value):
        self._encrypt_phone = value
    @property
    def pet_inst_id(self):
        return self._pet_inst_id

    @pet_inst_id.setter
    def pet_inst_id(self, value):
        self._pet_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypt_phone:
            if hasattr(self.encrypt_phone, 'to_alipay_dict'):
                params['encrypt_phone'] = self.encrypt_phone.to_alipay_dict()
            else:
                params['encrypt_phone'] = self.encrypt_phone
        if self.pet_inst_id:
            if hasattr(self.pet_inst_id, 'to_alipay_dict'):
                params['pet_inst_id'] = self.pet_inst_id.to_alipay_dict()
            else:
                params['pet_inst_id'] = self.pet_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOpenVoucherBizDataDTO()
        if 'encrypt_phone' in d:
            o.encrypt_phone = d['encrypt_phone']
        if 'pet_inst_id' in d:
            o.pet_inst_id = d['pet_inst_id']
        return o


