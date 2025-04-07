#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderUserinfoNpassporterDeleteModel(object):

    def __init__(self):
        self._identity_card = None
        self._out_biz_no = None
        self._phone = None
        self._project_id = None

    @property
    def identity_card(self):
        return self._identity_card

    @identity_card.setter
    def identity_card(self, value):
        self._identity_card = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        if isinstance(value, list):
            self._out_biz_no = list()
            for i in value:
                self._out_biz_no.append(i)
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity_card:
            if hasattr(self.identity_card, 'to_alipay_dict'):
                params['identity_card'] = self.identity_card.to_alipay_dict()
            else:
                params['identity_card'] = self.identity_card
        if self.out_biz_no:
            if isinstance(self.out_biz_no, list):
                for i in range(0, len(self.out_biz_no)):
                    element = self.out_biz_no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_biz_no[i] = element.to_alipay_dict()
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderUserinfoNpassporterDeleteModel()
        if 'identity_card' in d:
            o.identity_card = d['identity_card']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'phone' in d:
            o.phone = d['phone']
        if 'project_id' in d:
            o.project_id = d['project_id']
        return o


