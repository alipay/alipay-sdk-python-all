#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssistantGoodsVO import AssistantGoodsVO


class GoodsAssistantMsgContentVO(object):

    def __init__(self):
        self._goods_list = None
        self._recommend_text = None

    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, list):
            self._goods_list = list()
            for i in value:
                if isinstance(i, AssistantGoodsVO):
                    self._goods_list.append(i)
                else:
                    self._goods_list.append(AssistantGoodsVO.from_alipay_dict(i))
    @property
    def recommend_text(self):
        return self._recommend_text

    @recommend_text.setter
    def recommend_text(self, value):
        self._recommend_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_list:
            if isinstance(self.goods_list, list):
                for i in range(0, len(self.goods_list)):
                    element = self.goods_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_list, 'to_alipay_dict'):
                params['goods_list'] = self.goods_list.to_alipay_dict()
            else:
                params['goods_list'] = self.goods_list
        if self.recommend_text:
            if hasattr(self.recommend_text, 'to_alipay_dict'):
                params['recommend_text'] = self.recommend_text.to_alipay_dict()
            else:
                params['recommend_text'] = self.recommend_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsAssistantMsgContentVO()
        if 'goods_list' in d:
            o.goods_list = d['goods_list']
        if 'recommend_text' in d:
            o.recommend_text = d['recommend_text']
        return o


