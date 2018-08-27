#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbPosOrderDishDetail import KbPosOrderDishDetail
from alipay.aop.api.domain.PosOrderKey import PosOrderKey


class KoubeiCateringOrderInfoModifyModel(object):

    def __init__(self):
        self._action = None
        self._dish_details = None
        self._ext_info = None
        self._memo = None
        self._other_amount = None
        self._packing_amount = None
        self._people_num = None
        self._pos_order_key = None
        self._service_amount = None
        self._take_no = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def dish_details(self):
        return self._dish_details

    @dish_details.setter
    def dish_details(self, value):
        if isinstance(value, list):
            self._dish_details = list()
            for i in value:
                if isinstance(i, KbPosOrderDishDetail):
                    self._dish_details.append(i)
                else:
                    self._dish_details.append(KbPosOrderDishDetail.from_alipay_dict(i))
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def other_amount(self):
        return self._other_amount

    @other_amount.setter
    def other_amount(self, value):
        self._other_amount = value
    @property
    def packing_amount(self):
        return self._packing_amount

    @packing_amount.setter
    def packing_amount(self, value):
        self._packing_amount = value
    @property
    def people_num(self):
        return self._people_num

    @people_num.setter
    def people_num(self, value):
        self._people_num = value
    @property
    def pos_order_key(self):
        return self._pos_order_key

    @pos_order_key.setter
    def pos_order_key(self, value):
        if isinstance(value, PosOrderKey):
            self._pos_order_key = value
        else:
            self._pos_order_key = PosOrderKey.from_alipay_dict(value)
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def take_no(self):
        return self._take_no

    @take_no.setter
    def take_no(self, value):
        self._take_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.dish_details:
            if isinstance(self.dish_details, list):
                for i in range(0, len(self.dish_details)):
                    element = self.dish_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_details[i] = element.to_alipay_dict()
            if hasattr(self.dish_details, 'to_alipay_dict'):
                params['dish_details'] = self.dish_details.to_alipay_dict()
            else:
                params['dish_details'] = self.dish_details
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.other_amount:
            if hasattr(self.other_amount, 'to_alipay_dict'):
                params['other_amount'] = self.other_amount.to_alipay_dict()
            else:
                params['other_amount'] = self.other_amount
        if self.packing_amount:
            if hasattr(self.packing_amount, 'to_alipay_dict'):
                params['packing_amount'] = self.packing_amount.to_alipay_dict()
            else:
                params['packing_amount'] = self.packing_amount
        if self.people_num:
            if hasattr(self.people_num, 'to_alipay_dict'):
                params['people_num'] = self.people_num.to_alipay_dict()
            else:
                params['people_num'] = self.people_num
        if self.pos_order_key:
            if hasattr(self.pos_order_key, 'to_alipay_dict'):
                params['pos_order_key'] = self.pos_order_key.to_alipay_dict()
            else:
                params['pos_order_key'] = self.pos_order_key
        if self.service_amount:
            if hasattr(self.service_amount, 'to_alipay_dict'):
                params['service_amount'] = self.service_amount.to_alipay_dict()
            else:
                params['service_amount'] = self.service_amount
        if self.take_no:
            if hasattr(self.take_no, 'to_alipay_dict'):
                params['take_no'] = self.take_no.to_alipay_dict()
            else:
                params['take_no'] = self.take_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringOrderInfoModifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'dish_details' in d:
            o.dish_details = d['dish_details']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'memo' in d:
            o.memo = d['memo']
        if 'other_amount' in d:
            o.other_amount = d['other_amount']
        if 'packing_amount' in d:
            o.packing_amount = d['packing_amount']
        if 'people_num' in d:
            o.people_num = d['people_num']
        if 'pos_order_key' in d:
            o.pos_order_key = d['pos_order_key']
        if 'service_amount' in d:
            o.service_amount = d['service_amount']
        if 'take_no' in d:
            o.take_no = d['take_no']
        return o


