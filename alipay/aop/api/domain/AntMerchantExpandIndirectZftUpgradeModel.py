#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIndirectZftUpgradeModel(object):

    def __init__(self):
        self._additional_cert_image = None
        self._additional_cert_no = None
        self._additional_cert_type = None
        self._smid = None

    @property
    def additional_cert_image(self):
        return self._additional_cert_image

    @additional_cert_image.setter
    def additional_cert_image(self, value):
        self._additional_cert_image = value
    @property
    def additional_cert_no(self):
        return self._additional_cert_no

    @additional_cert_no.setter
    def additional_cert_no(self, value):
        self._additional_cert_no = value
    @property
    def additional_cert_type(self):
        return self._additional_cert_type

    @additional_cert_type.setter
    def additional_cert_type(self, value):
        self._additional_cert_type = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_cert_image:
            if hasattr(self.additional_cert_image, 'to_alipay_dict'):
                params['additional_cert_image'] = self.additional_cert_image.to_alipay_dict()
            else:
                params['additional_cert_image'] = self.additional_cert_image
        if self.additional_cert_no:
            if hasattr(self.additional_cert_no, 'to_alipay_dict'):
                params['additional_cert_no'] = self.additional_cert_no.to_alipay_dict()
            else:
                params['additional_cert_no'] = self.additional_cert_no
        if self.additional_cert_type:
            if hasattr(self.additional_cert_type, 'to_alipay_dict'):
                params['additional_cert_type'] = self.additional_cert_type.to_alipay_dict()
            else:
                params['additional_cert_type'] = self.additional_cert_type
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectZftUpgradeModel()
        if 'additional_cert_image' in d:
            o.additional_cert_image = d['additional_cert_image']
        if 'additional_cert_no' in d:
            o.additional_cert_no = d['additional_cert_no']
        if 'additional_cert_type' in d:
            o.additional_cert_type = d['additional_cert_type']
        if 'smid' in d:
            o.smid = d['smid']
        return o


