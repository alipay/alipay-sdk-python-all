#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingBenefitVerifyCreateModel(object):

    def __init__(self):
        self._biz_no = None
        self._call_back_url = None
        self._publisher_user_id = None
        self._risk_info = None
        self._verify_scene = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def call_back_url(self):
        return self._call_back_url

    @call_back_url.setter
    def call_back_url(self, value):
        self._call_back_url = value
    @property
    def publisher_user_id(self):
        return self._publisher_user_id

    @publisher_user_id.setter
    def publisher_user_id(self, value):
        self._publisher_user_id = value
    @property
    def risk_info(self):
        return self._risk_info

    @risk_info.setter
    def risk_info(self, value):
        self._risk_info = value
    @property
    def verify_scene(self):
        return self._verify_scene

    @verify_scene.setter
    def verify_scene(self, value):
        self._verify_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.call_back_url:
            if hasattr(self.call_back_url, 'to_alipay_dict'):
                params['call_back_url'] = self.call_back_url.to_alipay_dict()
            else:
                params['call_back_url'] = self.call_back_url
        if self.publisher_user_id:
            if hasattr(self.publisher_user_id, 'to_alipay_dict'):
                params['publisher_user_id'] = self.publisher_user_id.to_alipay_dict()
            else:
                params['publisher_user_id'] = self.publisher_user_id
        if self.risk_info:
            if hasattr(self.risk_info, 'to_alipay_dict'):
                params['risk_info'] = self.risk_info.to_alipay_dict()
            else:
                params['risk_info'] = self.risk_info
        if self.verify_scene:
            if hasattr(self.verify_scene, 'to_alipay_dict'):
                params['verify_scene'] = self.verify_scene.to_alipay_dict()
            else:
                params['verify_scene'] = self.verify_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingBenefitVerifyCreateModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'call_back_url' in d:
            o.call_back_url = d['call_back_url']
        if 'publisher_user_id' in d:
            o.publisher_user_id = d['publisher_user_id']
        if 'risk_info' in d:
            o.risk_info = d['risk_info']
        if 'verify_scene' in d:
            o.verify_scene = d['verify_scene']
        return o


