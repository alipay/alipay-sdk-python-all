#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayUserVO import CreditPayUserVO


class MybankCreditLoantradePayerBillrepayConsultModel(object):

    def __init__(self):
        self._bill_no = None
        self._biz_scene = None
        self._sub_biz_scene = None
        self._user_info = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, CreditPayUserVO):
            self._user_info = value
        else:
            self._user_info = CreditPayUserVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradePayerBillrepayConsultModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        if 'user_info' in d:
            o.user_info = d['user_info']
        return o


