#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CfbudmacBizActionConsumedAmountDTO import CfbudmacBizActionConsumedAmountDTO


class CfbudmacBizActionConsumedAmountsDTO(object):

    def __init__(self):
        self._biz_action_consumed_amount_list = None
        self._biz_uk_id = None

    @property
    def biz_action_consumed_amount_list(self):
        return self._biz_action_consumed_amount_list

    @biz_action_consumed_amount_list.setter
    def biz_action_consumed_amount_list(self, value):
        if isinstance(value, list):
            self._biz_action_consumed_amount_list = list()
            for i in value:
                if isinstance(i, CfbudmacBizActionConsumedAmountDTO):
                    self._biz_action_consumed_amount_list.append(i)
                else:
                    self._biz_action_consumed_amount_list.append(CfbudmacBizActionConsumedAmountDTO.from_alipay_dict(i))
    @property
    def biz_uk_id(self):
        return self._biz_uk_id

    @biz_uk_id.setter
    def biz_uk_id(self, value):
        self._biz_uk_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_action_consumed_amount_list:
            if isinstance(self.biz_action_consumed_amount_list, list):
                for i in range(0, len(self.biz_action_consumed_amount_list)):
                    element = self.biz_action_consumed_amount_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_action_consumed_amount_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_action_consumed_amount_list, 'to_alipay_dict'):
                params['biz_action_consumed_amount_list'] = self.biz_action_consumed_amount_list.to_alipay_dict()
            else:
                params['biz_action_consumed_amount_list'] = self.biz_action_consumed_amount_list
        if self.biz_uk_id:
            if hasattr(self.biz_uk_id, 'to_alipay_dict'):
                params['biz_uk_id'] = self.biz_uk_id.to_alipay_dict()
            else:
                params['biz_uk_id'] = self.biz_uk_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CfbudmacBizActionConsumedAmountsDTO()
        if 'biz_action_consumed_amount_list' in d:
            o.biz_action_consumed_amount_list = d['biz_action_consumed_amount_list']
        if 'biz_uk_id' in d:
            o.biz_uk_id = d['biz_uk_id']
        return o


