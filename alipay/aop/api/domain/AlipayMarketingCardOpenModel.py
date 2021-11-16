#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCard import MerchantCard
from alipay.aop.api.domain.CardUserInfo import CardUserInfo
from alipay.aop.api.domain.MerchantMenber import MerchantMenber
from alipay.aop.api.domain.PaidOuterCardExtraInfoDTO import PaidOuterCardExtraInfoDTO


class AlipayMarketingCardOpenModel(object):

    def __init__(self):
        self._card_ext_info = None
        self._card_template_id = None
        self._card_user_info = None
        self._member_ext_info = None
        self._open_card_channel = None
        self._open_card_channel_id = None
        self._out_serial_no = None
        self._paid_outer_card_info = None

    @property
    def card_ext_info(self):
        return self._card_ext_info

    @card_ext_info.setter
    def card_ext_info(self, value):
        if isinstance(value, MerchantCard):
            self._card_ext_info = value
        else:
            self._card_ext_info = MerchantCard.from_alipay_dict(value)
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def card_user_info(self):
        return self._card_user_info

    @card_user_info.setter
    def card_user_info(self, value):
        if isinstance(value, CardUserInfo):
            self._card_user_info = value
        else:
            self._card_user_info = CardUserInfo.from_alipay_dict(value)
    @property
    def member_ext_info(self):
        return self._member_ext_info

    @member_ext_info.setter
    def member_ext_info(self, value):
        if isinstance(value, MerchantMenber):
            self._member_ext_info = value
        else:
            self._member_ext_info = MerchantMenber.from_alipay_dict(value)
    @property
    def open_card_channel(self):
        return self._open_card_channel

    @open_card_channel.setter
    def open_card_channel(self, value):
        self._open_card_channel = value
    @property
    def open_card_channel_id(self):
        return self._open_card_channel_id

    @open_card_channel_id.setter
    def open_card_channel_id(self, value):
        self._open_card_channel_id = value
    @property
    def out_serial_no(self):
        return self._out_serial_no

    @out_serial_no.setter
    def out_serial_no(self, value):
        self._out_serial_no = value
    @property
    def paid_outer_card_info(self):
        return self._paid_outer_card_info

    @paid_outer_card_info.setter
    def paid_outer_card_info(self, value):
        if isinstance(value, PaidOuterCardExtraInfoDTO):
            self._paid_outer_card_info = value
        else:
            self._paid_outer_card_info = PaidOuterCardExtraInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.card_ext_info:
            if hasattr(self.card_ext_info, 'to_alipay_dict'):
                params['card_ext_info'] = self.card_ext_info.to_alipay_dict()
            else:
                params['card_ext_info'] = self.card_ext_info
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.card_user_info:
            if hasattr(self.card_user_info, 'to_alipay_dict'):
                params['card_user_info'] = self.card_user_info.to_alipay_dict()
            else:
                params['card_user_info'] = self.card_user_info
        if self.member_ext_info:
            if hasattr(self.member_ext_info, 'to_alipay_dict'):
                params['member_ext_info'] = self.member_ext_info.to_alipay_dict()
            else:
                params['member_ext_info'] = self.member_ext_info
        if self.open_card_channel:
            if hasattr(self.open_card_channel, 'to_alipay_dict'):
                params['open_card_channel'] = self.open_card_channel.to_alipay_dict()
            else:
                params['open_card_channel'] = self.open_card_channel
        if self.open_card_channel_id:
            if hasattr(self.open_card_channel_id, 'to_alipay_dict'):
                params['open_card_channel_id'] = self.open_card_channel_id.to_alipay_dict()
            else:
                params['open_card_channel_id'] = self.open_card_channel_id
        if self.out_serial_no:
            if hasattr(self.out_serial_no, 'to_alipay_dict'):
                params['out_serial_no'] = self.out_serial_no.to_alipay_dict()
            else:
                params['out_serial_no'] = self.out_serial_no
        if self.paid_outer_card_info:
            if hasattr(self.paid_outer_card_info, 'to_alipay_dict'):
                params['paid_outer_card_info'] = self.paid_outer_card_info.to_alipay_dict()
            else:
                params['paid_outer_card_info'] = self.paid_outer_card_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCardOpenModel()
        if 'card_ext_info' in d:
            o.card_ext_info = d['card_ext_info']
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'card_user_info' in d:
            o.card_user_info = d['card_user_info']
        if 'member_ext_info' in d:
            o.member_ext_info = d['member_ext_info']
        if 'open_card_channel' in d:
            o.open_card_channel = d['open_card_channel']
        if 'open_card_channel_id' in d:
            o.open_card_channel_id = d['open_card_channel_id']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'paid_outer_card_info' in d:
            o.paid_outer_card_info = d['paid_outer_card_info']
        return o


