#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KeyValuePair import KeyValuePair


class AlipayPcreditHuabeiBenefitOrderCreateModel(object):

    def __init__(self):
        self._alipay_biz_no = None
        self._alipay_user_id = None
        self._biz_param = None
        self._biz_time = None
        self._need_repeat = None
        self._out_goods_id = None
        self._out_request_no = None
        self._out_sku_id = None
        self._scene = None
        self._trigger_send = None

    @property
    def alipay_biz_no(self):
        return self._alipay_biz_no

    @alipay_biz_no.setter
    def alipay_biz_no(self, value):
        self._alipay_biz_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_param(self):
        return self._biz_param

    @biz_param.setter
    def biz_param(self, value):
        if isinstance(value, list):
            self._biz_param = list()
            for i in value:
                if isinstance(i, KeyValuePair):
                    self._biz_param.append(i)
                else:
                    self._biz_param.append(KeyValuePair.from_alipay_dict(i))
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def need_repeat(self):
        return self._need_repeat

    @need_repeat.setter
    def need_repeat(self, value):
        self._need_repeat = value
    @property
    def out_goods_id(self):
        return self._out_goods_id

    @out_goods_id.setter
    def out_goods_id(self, value):
        self._out_goods_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def trigger_send(self):
        return self._trigger_send

    @trigger_send.setter
    def trigger_send(self, value):
        self._trigger_send = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_biz_no:
            if hasattr(self.alipay_biz_no, 'to_alipay_dict'):
                params['alipay_biz_no'] = self.alipay_biz_no.to_alipay_dict()
            else:
                params['alipay_biz_no'] = self.alipay_biz_no
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_param:
            if isinstance(self.biz_param, list):
                for i in range(0, len(self.biz_param)):
                    element = self.biz_param[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_param[i] = element.to_alipay_dict()
            if hasattr(self.biz_param, 'to_alipay_dict'):
                params['biz_param'] = self.biz_param.to_alipay_dict()
            else:
                params['biz_param'] = self.biz_param
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.need_repeat:
            if hasattr(self.need_repeat, 'to_alipay_dict'):
                params['need_repeat'] = self.need_repeat.to_alipay_dict()
            else:
                params['need_repeat'] = self.need_repeat
        if self.out_goods_id:
            if hasattr(self.out_goods_id, 'to_alipay_dict'):
                params['out_goods_id'] = self.out_goods_id.to_alipay_dict()
            else:
                params['out_goods_id'] = self.out_goods_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.trigger_send:
            if hasattr(self.trigger_send, 'to_alipay_dict'):
                params['trigger_send'] = self.trigger_send.to_alipay_dict()
            else:
                params['trigger_send'] = self.trigger_send
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiBenefitOrderCreateModel()
        if 'alipay_biz_no' in d:
            o.alipay_biz_no = d['alipay_biz_no']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_param' in d:
            o.biz_param = d['biz_param']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'need_repeat' in d:
            o.need_repeat = d['need_repeat']
        if 'out_goods_id' in d:
            o.out_goods_id = d['out_goods_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'trigger_send' in d:
            o.trigger_send = d['trigger_send']
        return o


