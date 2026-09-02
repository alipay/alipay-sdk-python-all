#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDapplyOrderdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDapplyOrderdetailQueryResponse, self).__init__()
        self._address = None
        self._applicant_mobile = None
        self._applicant_name = None
        self._asset_apply_order_id = None
        self._batch_no = None
        self._city_code = None
        self._city_name = None
        self._district_code = None
        self._district_name = None
        self._gmt_create = None
        self._memo = None
        self._order_biz_id = None
        self._order_status = None
        self._province_code = None
        self._province_name = None
        self._receiver_mobile = None
        self._receiver_name = None
        self._shop_name = None
        self._status = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def applicant_mobile(self):
        return self._applicant_mobile

    @applicant_mobile.setter
    def applicant_mobile(self, value):
        self._applicant_mobile = value
    @property
    def applicant_name(self):
        return self._applicant_name

    @applicant_name.setter
    def applicant_name(self, value):
        self._applicant_name = value
    @property
    def asset_apply_order_id(self):
        return self._asset_apply_order_id

    @asset_apply_order_id.setter
    def asset_apply_order_id(self, value):
        self._asset_apply_order_id = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_biz_id(self):
        return self._order_biz_id

    @order_biz_id.setter
    def order_biz_id(self, value):
        self._order_biz_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def receiver_mobile(self):
        return self._receiver_mobile

    @receiver_mobile.setter
    def receiver_mobile(self, value):
        self._receiver_mobile = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDapplyOrderdetailQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'applicant_mobile' in response:
            self.applicant_mobile = response['applicant_mobile']
        if 'applicant_name' in response:
            self.applicant_name = response['applicant_name']
        if 'asset_apply_order_id' in response:
            self.asset_apply_order_id = response['asset_apply_order_id']
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'city_name' in response:
            self.city_name = response['city_name']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'district_name' in response:
            self.district_name = response['district_name']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'memo' in response:
            self.memo = response['memo']
        if 'order_biz_id' in response:
            self.order_biz_id = response['order_biz_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'province_name' in response:
            self.province_name = response['province_name']
        if 'receiver_mobile' in response:
            self.receiver_mobile = response['receiver_mobile']
        if 'receiver_name' in response:
            self.receiver_name = response['receiver_name']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'status' in response:
            self.status = response['status']
