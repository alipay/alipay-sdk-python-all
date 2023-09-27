#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SettleCardInfo import SettleCardInfo
from alipay.aop.api.domain.DefaultSettleRule import DefaultSettleRule


class AntMerchantExpandIndirectZftsubsettleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectZftsubsettleQueryResponse, self).__init__()
        self._alipay_logon_id = None
        self._alipay_logon_open_id = None
        self._alipay_logon_uid = None
        self._biz_cards = None
        self._default_settle_rule = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def alipay_logon_open_id(self):
        return self._alipay_logon_open_id

    @alipay_logon_open_id.setter
    def alipay_logon_open_id(self, value):
        self._alipay_logon_open_id = value
    @property
    def alipay_logon_uid(self):
        return self._alipay_logon_uid

    @alipay_logon_uid.setter
    def alipay_logon_uid(self, value):
        self._alipay_logon_uid = value
    @property
    def biz_cards(self):
        return self._biz_cards

    @biz_cards.setter
    def biz_cards(self, value):
        if isinstance(value, list):
            self._biz_cards = list()
            for i in value:
                if isinstance(i, SettleCardInfo):
                    self._biz_cards.append(i)
                else:
                    self._biz_cards.append(SettleCardInfo.from_alipay_dict(i))
    @property
    def default_settle_rule(self):
        return self._default_settle_rule

    @default_settle_rule.setter
    def default_settle_rule(self, value):
        if isinstance(value, DefaultSettleRule):
            self._default_settle_rule = value
        else:
            self._default_settle_rule = DefaultSettleRule.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectZftsubsettleQueryResponse, self).parse_response_content(response_content)
        if 'alipay_logon_id' in response:
            self.alipay_logon_id = response['alipay_logon_id']
        if 'alipay_logon_open_id' in response:
            self.alipay_logon_open_id = response['alipay_logon_open_id']
        if 'alipay_logon_uid' in response:
            self.alipay_logon_uid = response['alipay_logon_uid']
        if 'biz_cards' in response:
            self.biz_cards = response['biz_cards']
        if 'default_settle_rule' in response:
            self.default_settle_rule = response['default_settle_rule']
