#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitInfoDTO(object):

    def __init__(self):
        self._benefit_desc = None
        self._benefit_id = None
        self._benefit_img = None
        self._benefit_name = None
        self._benefit_status = None

    @property
    def benefit_desc(self):
        return self._benefit_desc

    @benefit_desc.setter
    def benefit_desc(self, value):
        self._benefit_desc = value
    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def benefit_img(self):
        return self._benefit_img

    @benefit_img.setter
    def benefit_img(self, value):
        self._benefit_img = value
    @property
    def benefit_name(self):
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, value):
        self._benefit_name = value
    @property
    def benefit_status(self):
        return self._benefit_status

    @benefit_status.setter
    def benefit_status(self, value):
        self._benefit_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_desc:
            if hasattr(self.benefit_desc, 'to_alipay_dict'):
                params['benefit_desc'] = self.benefit_desc.to_alipay_dict()
            else:
                params['benefit_desc'] = self.benefit_desc
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.benefit_img:
            if hasattr(self.benefit_img, 'to_alipay_dict'):
                params['benefit_img'] = self.benefit_img.to_alipay_dict()
            else:
                params['benefit_img'] = self.benefit_img
        if self.benefit_name:
            if hasattr(self.benefit_name, 'to_alipay_dict'):
                params['benefit_name'] = self.benefit_name.to_alipay_dict()
            else:
                params['benefit_name'] = self.benefit_name
        if self.benefit_status:
            if hasattr(self.benefit_status, 'to_alipay_dict'):
                params['benefit_status'] = self.benefit_status.to_alipay_dict()
            else:
                params['benefit_status'] = self.benefit_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitInfoDTO()
        if 'benefit_desc' in d:
            o.benefit_desc = d['benefit_desc']
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'benefit_img' in d:
            o.benefit_img = d['benefit_img']
        if 'benefit_name' in d:
            o.benefit_name = d['benefit_name']
        if 'benefit_status' in d:
            o.benefit_status = d['benefit_status']
        return o


