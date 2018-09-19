#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardFrontTextDTO import CardFrontTextDTO
from alipay.aop.api.domain.MdCodeInfoDTO import MdCodeInfoDTO


class MerchantCard(object):

    def __init__(self):
        self._balance = None
        self._biz_card_no = None
        self._external_card_no = None
        self._front_image_id = None
        self._front_text_list = None
        self._level = None
        self._mdcode_info = None
        self._open_date = None
        self._point = None
        self._template_id = None
        self._valid_date = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def biz_card_no(self):
        return self._biz_card_no

    @biz_card_no.setter
    def biz_card_no(self, value):
        self._biz_card_no = value
    @property
    def external_card_no(self):
        return self._external_card_no

    @external_card_no.setter
    def external_card_no(self, value):
        self._external_card_no = value
    @property
    def front_image_id(self):
        return self._front_image_id

    @front_image_id.setter
    def front_image_id(self, value):
        self._front_image_id = value
    @property
    def front_text_list(self):
        return self._front_text_list

    @front_text_list.setter
    def front_text_list(self, value):
        if isinstance(value, list):
            self._front_text_list = list()
            for i in value:
                if isinstance(i, CardFrontTextDTO):
                    self._front_text_list.append(i)
                else:
                    self._front_text_list.append(CardFrontTextDTO.from_alipay_dict(i))
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def mdcode_info(self):
        return self._mdcode_info

    @mdcode_info.setter
    def mdcode_info(self, value):
        if isinstance(value, MdCodeInfoDTO):
            self._mdcode_info = value
        else:
            self._mdcode_info = MdCodeInfoDTO.from_alipay_dict(value)
    @property
    def open_date(self):
        return self._open_date

    @open_date.setter
    def open_date(self, value):
        self._open_date = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        self._valid_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.biz_card_no:
            if hasattr(self.biz_card_no, 'to_alipay_dict'):
                params['biz_card_no'] = self.biz_card_no.to_alipay_dict()
            else:
                params['biz_card_no'] = self.biz_card_no
        if self.external_card_no:
            if hasattr(self.external_card_no, 'to_alipay_dict'):
                params['external_card_no'] = self.external_card_no.to_alipay_dict()
            else:
                params['external_card_no'] = self.external_card_no
        if self.front_image_id:
            if hasattr(self.front_image_id, 'to_alipay_dict'):
                params['front_image_id'] = self.front_image_id.to_alipay_dict()
            else:
                params['front_image_id'] = self.front_image_id
        if self.front_text_list:
            if isinstance(self.front_text_list, list):
                for i in range(0, len(self.front_text_list)):
                    element = self.front_text_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.front_text_list[i] = element.to_alipay_dict()
            if hasattr(self.front_text_list, 'to_alipay_dict'):
                params['front_text_list'] = self.front_text_list.to_alipay_dict()
            else:
                params['front_text_list'] = self.front_text_list
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.mdcode_info:
            if hasattr(self.mdcode_info, 'to_alipay_dict'):
                params['mdcode_info'] = self.mdcode_info.to_alipay_dict()
            else:
                params['mdcode_info'] = self.mdcode_info
        if self.open_date:
            if hasattr(self.open_date, 'to_alipay_dict'):
                params['open_date'] = self.open_date.to_alipay_dict()
            else:
                params['open_date'] = self.open_date
        if self.point:
            if hasattr(self.point, 'to_alipay_dict'):
                params['point'] = self.point.to_alipay_dict()
            else:
                params['point'] = self.point
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.valid_date:
            if hasattr(self.valid_date, 'to_alipay_dict'):
                params['valid_date'] = self.valid_date.to_alipay_dict()
            else:
                params['valid_date'] = self.valid_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantCard()
        if 'balance' in d:
            o.balance = d['balance']
        if 'biz_card_no' in d:
            o.biz_card_no = d['biz_card_no']
        if 'external_card_no' in d:
            o.external_card_no = d['external_card_no']
        if 'front_image_id' in d:
            o.front_image_id = d['front_image_id']
        if 'front_text_list' in d:
            o.front_text_list = d['front_text_list']
        if 'level' in d:
            o.level = d['level']
        if 'mdcode_info' in d:
            o.mdcode_info = d['mdcode_info']
        if 'open_date' in d:
            o.open_date = d['open_date']
        if 'point' in d:
            o.point = d['point']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'valid_date' in d:
            o.valid_date = d['valid_date']
        return o


