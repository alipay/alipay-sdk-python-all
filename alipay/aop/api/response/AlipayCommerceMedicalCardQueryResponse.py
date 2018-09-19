#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtendMedicalCard import ExtendMedicalCard


class AlipayCommerceMedicalCardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCardQueryResponse, self).__init__()
        self._agreement_no = None
        self._buyer_logon_id = None
        self._buyer_user_id = None
        self._card_org_name = None
        self._card_org_no = None
        self._city = None
        self._extend_cards = None
        self._extend_params = None
        self._gmt_sign = None
        self._medical_card_id = None
        self._medical_card_no = None
        self._medical_card_type = None
        self._out_user_card_no = None
        self._out_user_name = None
        self._sign_status = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def buyer_logon_id(self):
        return self._buyer_logon_id

    @buyer_logon_id.setter
    def buyer_logon_id(self, value):
        self._buyer_logon_id = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def card_org_name(self):
        return self._card_org_name

    @card_org_name.setter
    def card_org_name(self, value):
        self._card_org_name = value
    @property
    def card_org_no(self):
        return self._card_org_no

    @card_org_no.setter
    def card_org_no(self, value):
        self._card_org_no = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def extend_cards(self):
        return self._extend_cards

    @extend_cards.setter
    def extend_cards(self, value):
        if isinstance(value, list):
            self._extend_cards = list()
            for i in value:
                if isinstance(i, ExtendMedicalCard):
                    self._extend_cards.append(i)
                else:
                    self._extend_cards.append(ExtendMedicalCard.from_alipay_dict(i))
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def gmt_sign(self):
        return self._gmt_sign

    @gmt_sign.setter
    def gmt_sign(self, value):
        self._gmt_sign = value
    @property
    def medical_card_id(self):
        return self._medical_card_id

    @medical_card_id.setter
    def medical_card_id(self, value):
        self._medical_card_id = value
    @property
    def medical_card_no(self):
        return self._medical_card_no

    @medical_card_no.setter
    def medical_card_no(self, value):
        self._medical_card_no = value
    @property
    def medical_card_type(self):
        return self._medical_card_type

    @medical_card_type.setter
    def medical_card_type(self, value):
        self._medical_card_type = value
    @property
    def out_user_card_no(self):
        return self._out_user_card_no

    @out_user_card_no.setter
    def out_user_card_no(self, value):
        self._out_user_card_no = value
    @property
    def out_user_name(self):
        return self._out_user_name

    @out_user_name.setter
    def out_user_name(self, value):
        self._out_user_name = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCardQueryResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'buyer_logon_id' in response:
            self.buyer_logon_id = response['buyer_logon_id']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'card_org_name' in response:
            self.card_org_name = response['card_org_name']
        if 'card_org_no' in response:
            self.card_org_no = response['card_org_no']
        if 'city' in response:
            self.city = response['city']
        if 'extend_cards' in response:
            self.extend_cards = response['extend_cards']
        if 'extend_params' in response:
            self.extend_params = response['extend_params']
        if 'gmt_sign' in response:
            self.gmt_sign = response['gmt_sign']
        if 'medical_card_id' in response:
            self.medical_card_id = response['medical_card_id']
        if 'medical_card_no' in response:
            self.medical_card_no = response['medical_card_no']
        if 'medical_card_type' in response:
            self.medical_card_type = response['medical_card_type']
        if 'out_user_card_no' in response:
            self.out_user_card_no = response['out_user_card_no']
        if 'out_user_name' in response:
            self.out_user_name = response['out_user_name']
        if 'sign_status' in response:
            self.sign_status = response['sign_status']
