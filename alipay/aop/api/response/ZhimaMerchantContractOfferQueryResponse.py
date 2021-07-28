#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantContractOfferQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantContractOfferQueryResponse, self).__init__()
        self._category_code = None
        self._contract_content = None
        self._contract_principal_desc = None
        self._contract_principal_logo = None
        self._ext_info = None
        self._fufilment_callback_url = None
        self._fufilment_cnt = None
        self._fufilment_desc = None
        self._fufilment_end_time = None
        self._fufilment_period_type = None
        self._fufilment_start_time = None
        self._offer_creater_id = None
        self._offer_creater_name = None
        self._offer_creater_type = None
        self._out_biz_no = None
        self._out_content_no = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def contract_content(self):
        return self._contract_content

    @contract_content.setter
    def contract_content(self, value):
        self._contract_content = value
    @property
    def contract_principal_desc(self):
        return self._contract_principal_desc

    @contract_principal_desc.setter
    def contract_principal_desc(self, value):
        self._contract_principal_desc = value
    @property
    def contract_principal_logo(self):
        return self._contract_principal_logo

    @contract_principal_logo.setter
    def contract_principal_logo(self, value):
        self._contract_principal_logo = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def fufilment_callback_url(self):
        return self._fufilment_callback_url

    @fufilment_callback_url.setter
    def fufilment_callback_url(self, value):
        self._fufilment_callback_url = value
    @property
    def fufilment_cnt(self):
        return self._fufilment_cnt

    @fufilment_cnt.setter
    def fufilment_cnt(self, value):
        self._fufilment_cnt = value
    @property
    def fufilment_desc(self):
        return self._fufilment_desc

    @fufilment_desc.setter
    def fufilment_desc(self, value):
        self._fufilment_desc = value
    @property
    def fufilment_end_time(self):
        return self._fufilment_end_time

    @fufilment_end_time.setter
    def fufilment_end_time(self, value):
        self._fufilment_end_time = value
    @property
    def fufilment_period_type(self):
        return self._fufilment_period_type

    @fufilment_period_type.setter
    def fufilment_period_type(self, value):
        self._fufilment_period_type = value
    @property
    def fufilment_start_time(self):
        return self._fufilment_start_time

    @fufilment_start_time.setter
    def fufilment_start_time(self, value):
        self._fufilment_start_time = value
    @property
    def offer_creater_id(self):
        return self._offer_creater_id

    @offer_creater_id.setter
    def offer_creater_id(self, value):
        self._offer_creater_id = value
    @property
    def offer_creater_name(self):
        return self._offer_creater_name

    @offer_creater_name.setter
    def offer_creater_name(self, value):
        self._offer_creater_name = value
    @property
    def offer_creater_type(self):
        return self._offer_creater_type

    @offer_creater_type.setter
    def offer_creater_type(self, value):
        self._offer_creater_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_content_no(self):
        return self._out_content_no

    @out_content_no.setter
    def out_content_no(self, value):
        self._out_content_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantContractOfferQueryResponse, self).parse_response_content(response_content)
        if 'category_code' in response:
            self.category_code = response['category_code']
        if 'contract_content' in response:
            self.contract_content = response['contract_content']
        if 'contract_principal_desc' in response:
            self.contract_principal_desc = response['contract_principal_desc']
        if 'contract_principal_logo' in response:
            self.contract_principal_logo = response['contract_principal_logo']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'fufilment_callback_url' in response:
            self.fufilment_callback_url = response['fufilment_callback_url']
        if 'fufilment_cnt' in response:
            self.fufilment_cnt = response['fufilment_cnt']
        if 'fufilment_desc' in response:
            self.fufilment_desc = response['fufilment_desc']
        if 'fufilment_end_time' in response:
            self.fufilment_end_time = response['fufilment_end_time']
        if 'fufilment_period_type' in response:
            self.fufilment_period_type = response['fufilment_period_type']
        if 'fufilment_start_time' in response:
            self.fufilment_start_time = response['fufilment_start_time']
        if 'offer_creater_id' in response:
            self.offer_creater_id = response['offer_creater_id']
        if 'offer_creater_name' in response:
            self.offer_creater_name = response['offer_creater_name']
        if 'offer_creater_type' in response:
            self.offer_creater_type = response['offer_creater_type']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'out_content_no' in response:
            self.out_content_no = response['out_content_no']
