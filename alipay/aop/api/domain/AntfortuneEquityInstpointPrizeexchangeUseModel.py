#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneEquityInstpointPrizeexchangeUseModel(object):

    def __init__(self):
        self._mobile = None
        self._out_biz_no = None
        self._prize_no = None
        self._user_id = None

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def prize_no(self):
        return self._prize_no

    @prize_no.setter
    def prize_no(self, value):
        self._prize_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.prize_no:
            if hasattr(self.prize_no, 'to_alipay_dict'):
                params['prize_no'] = self.prize_no.to_alipay_dict()
            else:
                params['prize_no'] = self.prize_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneEquityInstpointPrizeexchangeUseModel()
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'prize_no' in d:
            o.prize_no = d['prize_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


