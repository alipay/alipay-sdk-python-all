#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoyagerEnvInfo import VoyagerEnvInfo
from alipay.aop.api.domain.VoyagerGoodsInfo import VoyagerGoodsInfo


class AlipayVoyagerMarketingBatchconsultModel(object):

    def __init__(self):
        self._channel = None
        self._env_info = None
        self._goods_info_list = None
        self._industry = None
        self._language = None
        self._open_id = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.env_info:
            if hasattr(self.env_info, 'to_alipay_dict'):
                params['env_info'] = self.env_info.to_alipay_dict()
            else:
                params['env_info'] = self.env_info
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
        o = AlipayVoyagerMarketingBatchconsultModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'env_info' in d:
            o.env_info = d['env_info']
        if 'goods_info_list' in d:
            o.goods_info_list = d['goods_info_list']
        if 'industry' in d:
            o.industry = d['industry']
        if 'language' in d:
            o.language = d['language']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


