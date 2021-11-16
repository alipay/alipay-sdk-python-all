#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCard import MerchantCard
from alipay.aop.api.domain.McardStylInfo import McardStylInfo
from alipay.aop.api.domain.MerchantCardMsgInfo import MerchantCardMsgInfo
from alipay.aop.api.domain.McardNotifyMessage import McardNotifyMessage
from alipay.aop.api.domain.PaidOuterCardExtraInfoDTO import PaidOuterCardExtraInfoDTO


class AlipayMarketingCardUpdateModel(object):

    def __init__(self):
        self._card_info = None
        self._ext_info = None
        self._mcard_style_info = None
        self._merchant_card_msg_info = None
        self._notify_messages = None
        self._occur_time = None
        self._paid_outer_card_info = None
        self._target_card_no = None
        self._target_card_no_type = None

    @property
    def card_info(self):
        return self._card_info

    @card_info.setter
    def card_info(self, value):
        if isinstance(value, MerchantCard):
            self._card_info = value
        else:
            self._card_info = MerchantCard.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def mcard_style_info(self):
        return self._mcard_style_info

    @mcard_style_info.setter
    def mcard_style_info(self, value):
        if isinstance(value, McardStylInfo):
            self._mcard_style_info = value
        else:
            self._mcard_style_info = McardStylInfo.from_alipay_dict(value)
    @property
    def merchant_card_msg_info(self):
        return self._merchant_card_msg_info

    @merchant_card_msg_info.setter
    def merchant_card_msg_info(self, value):
        if isinstance(value, MerchantCardMsgInfo):
            self._merchant_card_msg_info = value
        else:
            self._merchant_card_msg_info = MerchantCardMsgInfo.from_alipay_dict(value)
    @property
    def notify_messages(self):
        return self._notify_messages

    @notify_messages.setter
    def notify_messages(self, value):
        if isinstance(value, list):
            self._notify_messages = list()
            for i in value:
                if isinstance(i, McardNotifyMessage):
                    self._notify_messages.append(i)
                else:
                    self._notify_messages.append(McardNotifyMessage.from_alipay_dict(i))
    @property
    def occur_time(self):
        return self._occur_time

    @occur_time.setter
    def occur_time(self, value):
        self._occur_time = value
    @property
    def paid_outer_card_info(self):
        return self._paid_outer_card_info

    @paid_outer_card_info.setter
    def paid_outer_card_info(self, value):
        if isinstance(value, PaidOuterCardExtraInfoDTO):
            self._paid_outer_card_info = value
        else:
            self._paid_outer_card_info = PaidOuterCardExtraInfoDTO.from_alipay_dict(value)
    @property
    def target_card_no(self):
        return self._target_card_no

    @target_card_no.setter
    def target_card_no(self, value):
        self._target_card_no = value
    @property
    def target_card_no_type(self):
        return self._target_card_no_type

    @target_card_no_type.setter
    def target_card_no_type(self, value):
        self._target_card_no_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_info:
            if hasattr(self.card_info, 'to_alipay_dict'):
                params['card_info'] = self.card_info.to_alipay_dict()
            else:
                params['card_info'] = self.card_info
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.mcard_style_info:
            if hasattr(self.mcard_style_info, 'to_alipay_dict'):
                params['mcard_style_info'] = self.mcard_style_info.to_alipay_dict()
            else:
                params['mcard_style_info'] = self.mcard_style_info
        if self.merchant_card_msg_info:
            if hasattr(self.merchant_card_msg_info, 'to_alipay_dict'):
                params['merchant_card_msg_info'] = self.merchant_card_msg_info.to_alipay_dict()
            else:
                params['merchant_card_msg_info'] = self.merchant_card_msg_info
        if self.notify_messages:
            if isinstance(self.notify_messages, list):
                for i in range(0, len(self.notify_messages)):
                    element = self.notify_messages[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.notify_messages[i] = element.to_alipay_dict()
            if hasattr(self.notify_messages, 'to_alipay_dict'):
                params['notify_messages'] = self.notify_messages.to_alipay_dict()
            else:
                params['notify_messages'] = self.notify_messages
        if self.occur_time:
            if hasattr(self.occur_time, 'to_alipay_dict'):
                params['occur_time'] = self.occur_time.to_alipay_dict()
            else:
                params['occur_time'] = self.occur_time
        if self.paid_outer_card_info:
            if hasattr(self.paid_outer_card_info, 'to_alipay_dict'):
                params['paid_outer_card_info'] = self.paid_outer_card_info.to_alipay_dict()
            else:
                params['paid_outer_card_info'] = self.paid_outer_card_info
        if self.target_card_no:
            if hasattr(self.target_card_no, 'to_alipay_dict'):
                params['target_card_no'] = self.target_card_no.to_alipay_dict()
            else:
                params['target_card_no'] = self.target_card_no
        if self.target_card_no_type:
            if hasattr(self.target_card_no_type, 'to_alipay_dict'):
                params['target_card_no_type'] = self.target_card_no_type.to_alipay_dict()
            else:
                params['target_card_no_type'] = self.target_card_no_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCardUpdateModel()
        if 'card_info' in d:
            o.card_info = d['card_info']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'mcard_style_info' in d:
            o.mcard_style_info = d['mcard_style_info']
        if 'merchant_card_msg_info' in d:
            o.merchant_card_msg_info = d['merchant_card_msg_info']
        if 'notify_messages' in d:
            o.notify_messages = d['notify_messages']
        if 'occur_time' in d:
            o.occur_time = d['occur_time']
        if 'paid_outer_card_info' in d:
            o.paid_outer_card_info = d['paid_outer_card_info']
        if 'target_card_no' in d:
            o.target_card_no = d['target_card_no']
        if 'target_card_no_type' in d:
            o.target_card_no_type = d['target_card_no_type']
        return o


