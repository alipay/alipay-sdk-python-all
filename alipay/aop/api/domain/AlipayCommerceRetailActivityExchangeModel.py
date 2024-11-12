#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailActivityExchangeModel(object):

    def __init__(self):
        self._biz_no = None
        self._open_id = None
        self._prize_id = None
        self._retail_activity_id = None
        self._transfer_info = None
        self._user_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def retail_activity_id(self):
        return self._retail_activity_id

    @retail_activity_id.setter
    def retail_activity_id(self, value):
        self._retail_activity_id = value
    @property
    def transfer_info(self):
        return self._transfer_info

    @transfer_info.setter
    def transfer_info(self, value):
        self._transfer_info = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.retail_activity_id:
            if hasattr(self.retail_activity_id, 'to_alipay_dict'):
                params['retail_activity_id'] = self.retail_activity_id.to_alipay_dict()
            else:
                params['retail_activity_id'] = self.retail_activity_id
        if self.transfer_info:
            if hasattr(self.transfer_info, 'to_alipay_dict'):
                params['transfer_info'] = self.transfer_info.to_alipay_dict()
            else:
                params['transfer_info'] = self.transfer_info
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
        o = AlipayCommerceRetailActivityExchangeModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'retail_activity_id' in d:
            o.retail_activity_id = d['retail_activity_id']
        if 'transfer_info' in d:
            o.transfer_info = d['transfer_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


