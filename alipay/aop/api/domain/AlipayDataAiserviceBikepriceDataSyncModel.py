#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MakePriceExtParams import MakePriceExtParams


class AlipayDataAiserviceBikepriceDataSyncModel(object):

    def __init__(self):
        self._ad_source = None
        self._base_price = None
        self._biz_time = None
        self._card_type = None
        self._card_type_version = None
        self._city_code = None
        self._make_price_ext_params = None
        self._op_type = None
        self._out_user_id = None
        self._plat_form = None
        self._priority = None
        self._promo_channel = None
        self._promotion_price = None
        self._promotion_type = None
        self._scene_code = None
        self._service_name = None
        self._source = None
        self._system_code = None
        self._trace_id = None
        self._user_attribute = None
        self._user_id = None
        self._valid_time = None

    @property
    def ad_source(self):
        return self._ad_source

    @ad_source.setter
    def ad_source(self, value):
        self._ad_source = value
    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        self._base_price = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def card_type_version(self):
        return self._card_type_version

    @card_type_version.setter
    def card_type_version(self, value):
        self._card_type_version = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def make_price_ext_params(self):
        return self._make_price_ext_params

    @make_price_ext_params.setter
    def make_price_ext_params(self, value):
        if isinstance(value, MakePriceExtParams):
            self._make_price_ext_params = value
        else:
            self._make_price_ext_params = MakePriceExtParams.from_alipay_dict(value)
    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, value):
        self._op_type = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def plat_form(self):
        return self._plat_form

    @plat_form.setter
    def plat_form(self, value):
        self._plat_form = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def promo_channel(self):
        return self._promo_channel

    @promo_channel.setter
    def promo_channel(self, value):
        self._promo_channel = value
    @property
    def promotion_price(self):
        return self._promotion_price

    @promotion_price.setter
    def promotion_price(self, value):
        self._promotion_price = value
    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def system_code(self):
        return self._system_code

    @system_code.setter
    def system_code(self, value):
        self._system_code = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def user_attribute(self):
        return self._user_attribute

    @user_attribute.setter
    def user_attribute(self, value):
        self._user_attribute = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_source:
            if hasattr(self.ad_source, 'to_alipay_dict'):
                params['ad_source'] = self.ad_source.to_alipay_dict()
            else:
                params['ad_source'] = self.ad_source
        if self.base_price:
            if hasattr(self.base_price, 'to_alipay_dict'):
                params['base_price'] = self.base_price.to_alipay_dict()
            else:
                params['base_price'] = self.base_price
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.card_type_version:
            if hasattr(self.card_type_version, 'to_alipay_dict'):
                params['card_type_version'] = self.card_type_version.to_alipay_dict()
            else:
                params['card_type_version'] = self.card_type_version
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.make_price_ext_params:
            if hasattr(self.make_price_ext_params, 'to_alipay_dict'):
                params['make_price_ext_params'] = self.make_price_ext_params.to_alipay_dict()
            else:
                params['make_price_ext_params'] = self.make_price_ext_params
        if self.op_type:
            if hasattr(self.op_type, 'to_alipay_dict'):
                params['op_type'] = self.op_type.to_alipay_dict()
            else:
                params['op_type'] = self.op_type
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.plat_form:
            if hasattr(self.plat_form, 'to_alipay_dict'):
                params['plat_form'] = self.plat_form.to_alipay_dict()
            else:
                params['plat_form'] = self.plat_form
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.promo_channel:
            if hasattr(self.promo_channel, 'to_alipay_dict'):
                params['promo_channel'] = self.promo_channel.to_alipay_dict()
            else:
                params['promo_channel'] = self.promo_channel
        if self.promotion_price:
            if hasattr(self.promotion_price, 'to_alipay_dict'):
                params['promotion_price'] = self.promotion_price.to_alipay_dict()
            else:
                params['promotion_price'] = self.promotion_price
        if self.promotion_type:
            if hasattr(self.promotion_type, 'to_alipay_dict'):
                params['promotion_type'] = self.promotion_type.to_alipay_dict()
            else:
                params['promotion_type'] = self.promotion_type
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.system_code:
            if hasattr(self.system_code, 'to_alipay_dict'):
                params['system_code'] = self.system_code.to_alipay_dict()
            else:
                params['system_code'] = self.system_code
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        if self.user_attribute:
            if hasattr(self.user_attribute, 'to_alipay_dict'):
                params['user_attribute'] = self.user_attribute.to_alipay_dict()
            else:
                params['user_attribute'] = self.user_attribute
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.valid_time:
            if hasattr(self.valid_time, 'to_alipay_dict'):
                params['valid_time'] = self.valid_time.to_alipay_dict()
            else:
                params['valid_time'] = self.valid_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceBikepriceDataSyncModel()
        if 'ad_source' in d:
            o.ad_source = d['ad_source']
        if 'base_price' in d:
            o.base_price = d['base_price']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'card_type_version' in d:
            o.card_type_version = d['card_type_version']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'make_price_ext_params' in d:
            o.make_price_ext_params = d['make_price_ext_params']
        if 'op_type' in d:
            o.op_type = d['op_type']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'plat_form' in d:
            o.plat_form = d['plat_form']
        if 'priority' in d:
            o.priority = d['priority']
        if 'promo_channel' in d:
            o.promo_channel = d['promo_channel']
        if 'promotion_price' in d:
            o.promotion_price = d['promotion_price']
        if 'promotion_type' in d:
            o.promotion_type = d['promotion_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'source' in d:
            o.source = d['source']
        if 'system_code' in d:
            o.system_code = d['system_code']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'user_attribute' in d:
            o.user_attribute = d['user_attribute']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'valid_time' in d:
            o.valid_time = d['valid_time']
        return o


