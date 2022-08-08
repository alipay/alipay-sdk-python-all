#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UniCardFixVoucherInfo import UniCardFixVoucherInfo


class AlipayMarketingCampaignUnicardCardConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignUnicardCardConsultResponse, self).__init__()
        self._card_status = None
        self._card_template_id = None
        self._city_code = None
        self._consult_result_code = None
        self._expire_date = None
        self._fix_voucher_infos = None
        self._sale_price = None
        self._sub_card_status = None
        self._uni_card_no = None
        self._user_id = None

    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def consult_result_code(self):
        return self._consult_result_code

    @consult_result_code.setter
    def consult_result_code(self, value):
        self._consult_result_code = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def fix_voucher_infos(self):
        return self._fix_voucher_infos

    @fix_voucher_infos.setter
    def fix_voucher_infos(self, value):
        if isinstance(value, list):
            self._fix_voucher_infos = list()
            for i in value:
                if isinstance(i, UniCardFixVoucherInfo):
                    self._fix_voucher_infos.append(i)
                else:
                    self._fix_voucher_infos.append(UniCardFixVoucherInfo.from_alipay_dict(i))
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sub_card_status(self):
        return self._sub_card_status

    @sub_card_status.setter
    def sub_card_status(self, value):
        self._sub_card_status = value
    @property
    def uni_card_no(self):
        return self._uni_card_no

    @uni_card_no.setter
    def uni_card_no(self, value):
        self._uni_card_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignUnicardCardConsultResponse, self).parse_response_content(response_content)
        if 'card_status' in response:
            self.card_status = response['card_status']
        if 'card_template_id' in response:
            self.card_template_id = response['card_template_id']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'consult_result_code' in response:
            self.consult_result_code = response['consult_result_code']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'fix_voucher_infos' in response:
            self.fix_voucher_infos = response['fix_voucher_infos']
        if 'sale_price' in response:
            self.sale_price = response['sale_price']
        if 'sub_card_status' in response:
            self.sub_card_status = response['sub_card_status']
        if 'uni_card_no' in response:
            self.uni_card_no = response['uni_card_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
