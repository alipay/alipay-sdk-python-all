#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandZftChargerelationBindModel(object):

    def __init__(self):
        self._license_auth_letter_image = None
        self._smid = None
        self._target_smid = None

    @property
    def license_auth_letter_image(self):
        return self._license_auth_letter_image

    @license_auth_letter_image.setter
    def license_auth_letter_image(self, value):
        self._license_auth_letter_image = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def target_smid(self):
        return self._target_smid

    @target_smid.setter
    def target_smid(self, value):
        self._target_smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.license_auth_letter_image:
            if hasattr(self.license_auth_letter_image, 'to_alipay_dict'):
                params['license_auth_letter_image'] = self.license_auth_letter_image.to_alipay_dict()
            else:
                params['license_auth_letter_image'] = self.license_auth_letter_image
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.target_smid:
            if hasattr(self.target_smid, 'to_alipay_dict'):
                params['target_smid'] = self.target_smid.to_alipay_dict()
            else:
                params['target_smid'] = self.target_smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandZftChargerelationBindModel()
        if 'license_auth_letter_image' in d:
            o.license_auth_letter_image = d['license_auth_letter_image']
        if 'smid' in d:
            o.smid = d['smid']
        if 'target_smid' in d:
            o.target_smid = d['target_smid']
        return o


