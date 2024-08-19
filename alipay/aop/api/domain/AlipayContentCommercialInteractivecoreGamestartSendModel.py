#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GiftBatchInfo import GiftBatchInfo


class AlipayContentCommercialInteractivecoreGamestartSendModel(object):

    def __init__(self):
        self._biz_token = None
        self._gift_batch_info = None
        self._msg_id = None
        self._ts = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def gift_batch_info(self):
        return self._gift_batch_info

    @gift_batch_info.setter
    def gift_batch_info(self, value):
        if isinstance(value, list):
            self._gift_batch_info = list()
            for i in value:
                if isinstance(i, GiftBatchInfo):
                    self._gift_batch_info.append(i)
                else:
                    self._gift_batch_info.append(GiftBatchInfo.from_alipay_dict(i))
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def ts(self):
        return self._ts

    @ts.setter
    def ts(self, value):
        self._ts = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.gift_batch_info:
            if isinstance(self.gift_batch_info, list):
                for i in range(0, len(self.gift_batch_info)):
                    element = self.gift_batch_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gift_batch_info[i] = element.to_alipay_dict()
            if hasattr(self.gift_batch_info, 'to_alipay_dict'):
                params['gift_batch_info'] = self.gift_batch_info.to_alipay_dict()
            else:
                params['gift_batch_info'] = self.gift_batch_info
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.ts:
            if hasattr(self.ts, 'to_alipay_dict'):
                params['ts'] = self.ts.to_alipay_dict()
            else:
                params['ts'] = self.ts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentCommercialInteractivecoreGamestartSendModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'gift_batch_info' in d:
            o.gift_batch_info = d['gift_batch_info']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'ts' in d:
            o.ts = d['ts']
        return o


