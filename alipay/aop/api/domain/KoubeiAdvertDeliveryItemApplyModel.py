#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiAdvertDeliveryItemApplyModel(object):

    def __init__(self):
        self._adv_id = None
        self._channel_code = None
        self._channel_id = None
        self._out_biz_no = None
        self._recommend_id = None
        self._shop_id = None
        self._tag = None

    @property
    def adv_id(self):
        return self._adv_id

    @adv_id.setter
    def adv_id(self, value):
        self._adv_id = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def recommend_id(self):
        return self._recommend_id

    @recommend_id.setter
    def recommend_id(self, value):
        self._recommend_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.adv_id:
            if hasattr(self.adv_id, 'to_alipay_dict'):
                params['adv_id'] = self.adv_id.to_alipay_dict()
            else:
                params['adv_id'] = self.adv_id
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.recommend_id:
            if hasattr(self.recommend_id, 'to_alipay_dict'):
                params['recommend_id'] = self.recommend_id.to_alipay_dict()
            else:
                params['recommend_id'] = self.recommend_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertDeliveryItemApplyModel()
        if 'adv_id' in d:
            o.adv_id = d['adv_id']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'recommend_id' in d:
            o.recommend_id = d['recommend_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'tag' in d:
            o.tag = d['tag']
        return o


