#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JAPaymentInfo import JAPaymentInfo


class AlipayFundJointaccountRelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountRelationQueryResponse, self).__init__()
        self._account_id = None
        self._invitee_id = None
        self._invitee_open_id = None
        self._invitee_out_id = None
        self._inviter_id = None
        self._inviter_open_id = None
        self._inviter_out_id = None
        self._payment_info = None
        self._relation_id = None
        self._relation_status = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def invitee_id(self):
        return self._invitee_id

    @invitee_id.setter
    def invitee_id(self, value):
        self._invitee_id = value
    @property
    def invitee_open_id(self):
        return self._invitee_open_id

    @invitee_open_id.setter
    def invitee_open_id(self, value):
        self._invitee_open_id = value
    @property
    def invitee_out_id(self):
        return self._invitee_out_id

    @invitee_out_id.setter
    def invitee_out_id(self, value):
        self._invitee_out_id = value
    @property
    def inviter_id(self):
        return self._inviter_id

    @inviter_id.setter
    def inviter_id(self, value):
        self._inviter_id = value
    @property
    def inviter_open_id(self):
        return self._inviter_open_id

    @inviter_open_id.setter
    def inviter_open_id(self, value):
        self._inviter_open_id = value
    @property
    def inviter_out_id(self):
        return self._inviter_out_id

    @inviter_out_id.setter
    def inviter_out_id(self, value):
        self._inviter_out_id = value
    @property
    def payment_info(self):
        return self._payment_info

    @payment_info.setter
    def payment_info(self, value):
        if isinstance(value, JAPaymentInfo):
            self._payment_info = value
        else:
            self._payment_info = JAPaymentInfo.from_alipay_dict(value)
    @property
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, value):
        self._relation_id = value
    @property
    def relation_status(self):
        return self._relation_status

    @relation_status.setter
    def relation_status(self, value):
        self._relation_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountRelationQueryResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'invitee_id' in response:
            self.invitee_id = response['invitee_id']
        if 'invitee_open_id' in response:
            self.invitee_open_id = response['invitee_open_id']
        if 'invitee_out_id' in response:
            self.invitee_out_id = response['invitee_out_id']
        if 'inviter_id' in response:
            self.inviter_id = response['inviter_id']
        if 'inviter_open_id' in response:
            self.inviter_open_id = response['inviter_open_id']
        if 'inviter_out_id' in response:
            self.inviter_out_id = response['inviter_out_id']
        if 'payment_info' in response:
            self.payment_info = response['payment_info']
        if 'relation_id' in response:
            self.relation_id = response['relation_id']
        if 'relation_status' in response:
            self.relation_status = response['relation_status']
