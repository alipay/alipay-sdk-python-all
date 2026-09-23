#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoyagerEnvInfo import VoyagerEnvInfo
from alipay.aop.api.domain.VoyagerGoodsInfo import VoyagerGoodsInfo
from alipay.aop.api.domain.OrderPriceParam import OrderPriceParam


class AlipayVoyagerMarketingConsultModel(object):

    def __init__(self):
        self._biz_date = None
        self._channel = None
        self._consult_request_id = None
        self._env_info = None
        self._extend_info = None
        self._goods_info_list = None
        self._industry = None
        self._language = None
        self._open_id = None
        self._order_price_param = None
        self._user_id = None
        self._voucher_ids = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def consult_request_id(self):
        return self._consult_request_id

    @consult_request_id.setter
    def consult_request_id(self, value):
        self._consult_request_id = value
    @property
    def env_info(self):
        return self._env_info

    @env_info.setter
    def env_info(self, value):
        if isinstance(value, VoyagerEnvInfo):
            self._env_info = value
        else:
            self._env_info = VoyagerEnvInfo.from_alipay_dict(value)
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def goods_info_list(self):
        return self._goods_info_list

    @goods_info_list.setter
    def goods_info_list(self, value):
        if isinstance(value, list):
            self._goods_info_list = list()
            for i in value:
                if isinstance(i, VoyagerGoodsInfo):
                    self._goods_info_list.append(i)
                else:
                    self._goods_info_list.append(VoyagerGoodsInfo.from_alipay_dict(i))
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_price_param(self):
        return self._order_price_param

    @order_price_param.setter
    def order_price_param(self, value):
        if isinstance(value, OrderPriceParam):
            self._order_price_param = value
        else:
            self._order_price_param = OrderPriceParam.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voucher_ids(self):
        return self._voucher_ids

    @voucher_ids.setter
    def voucher_ids(self, value):
        if isinstance(value, list):
            self._voucher_ids = list()
            for i in value:
                self._voucher_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.consult_request_id:
            if hasattr(self.consult_request_id, 'to_alipay_dict'):
                params['consult_request_id'] = self.consult_request_id.to_alipay_dict()
            else:
                params['consult_request_id'] = self.consult_request_id
        if self.env_info:
            if hasattr(self.env_info, 'to_alipay_dict'):
                params['env_info'] = self.env_info.to_alipay_dict()
            else:
                params['env_info'] = self.env_info
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.goods_info_list:
            if isinstance(self.goods_info_list, list):
                for i in range(0, len(self.goods_info_list)):
                    element = self.goods_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_info_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_info_list, 'to_alipay_dict'):
                params['goods_info_list'] = self.goods_info_list.to_alipay_dict()
            else:
                params['goods_info_list'] = self.goods_info_list
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.language:
            if hasattr(self.language, 'to_alipay_dict'):
                params['language'] = self.language.to_alipay_dict()
            else:
                params['language'] = self.language
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_price_param:
            if hasattr(self.order_price_param, 'to_alipay_dict'):
                params['order_price_param'] = self.order_price_param.to_alipay_dict()
            else:
                params['order_price_param'] = self.order_price_param
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.voucher_ids:
            if isinstance(self.voucher_ids, list):
                for i in range(0, len(self.voucher_ids)):
                    element = self.voucher_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_ids[i] = element.to_alipay_dict()
            if hasattr(self.voucher_ids, 'to_alipay_dict'):
                params['voucher_ids'] = self.voucher_ids.to_alipay_dict()
            else:
                params['voucher_ids'] = self.voucher_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayVoyagerMarketingConsultModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'channel' in d:
            o.channel = d['channel']
        if 'consult_request_id' in d:
            o.consult_request_id = d['consult_request_id']
        if 'env_info' in d:
            o.env_info = d['env_info']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'goods_info_list' in d:
            o.goods_info_list = d['goods_info_list']
        if 'industry' in d:
            o.industry = d['industry']
        if 'language' in d:
            o.language = d['language']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_price_param' in d:
            o.order_price_param = d['order_price_param']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'voucher_ids' in d:
            o.voucher_ids = d['voucher_ids']
        return o


