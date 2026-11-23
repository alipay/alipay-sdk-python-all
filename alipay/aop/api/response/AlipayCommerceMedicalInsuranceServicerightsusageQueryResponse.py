#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceServicerightsusageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceServicerightsusageQueryResponse, self).__init__()
        self._available_stock = None
        self._event_id = None
        self._first_use_time = None
        self._fulfillment_data = None
        self._fulfillment_id = None
        self._fulfillment_name = None
        self._fulfillment_status = None
        self._fulfillment_type = None
        self._occur_time = None
        self._open_id = None
        self._out_unique_biz_no = None
        self._service_item_id = None
        self._unique_biz_no = None
        self._used_times = None
        self._user_id = None

    @property
    def available_stock(self):
        return self._available_stock

    @available_stock.setter
    def available_stock(self, value):
        self._available_stock = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def first_use_time(self):
        return self._first_use_time

    @first_use_time.setter
    def first_use_time(self, value):
        self._first_use_time = value
    @property
    def fulfillment_data(self):
        return self._fulfillment_data

    @fulfillment_data.setter
    def fulfillment_data(self, value):
        self._fulfillment_data = value
    @property
    def fulfillment_id(self):
        return self._fulfillment_id

    @fulfillment_id.setter
    def fulfillment_id(self, value):
        self._fulfillment_id = value
    @property
    def fulfillment_name(self):
        return self._fulfillment_name

    @fulfillment_name.setter
    def fulfillment_name(self, value):
        self._fulfillment_name = value
    @property
    def fulfillment_status(self):
        return self._fulfillment_status

    @fulfillment_status.setter
    def fulfillment_status(self, value):
        self._fulfillment_status = value
    @property
    def fulfillment_type(self):
        return self._fulfillment_type

    @fulfillment_type.setter
    def fulfillment_type(self, value):
        self._fulfillment_type = value
    @property
    def occur_time(self):
        return self._occur_time

    @occur_time.setter
    def occur_time(self, value):
        self._occur_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_unique_biz_no(self):
        return self._out_unique_biz_no

    @out_unique_biz_no.setter
    def out_unique_biz_no(self, value):
        self._out_unique_biz_no = value
    @property
    def service_item_id(self):
        return self._service_item_id

    @service_item_id.setter
    def service_item_id(self, value):
        self._service_item_id = value
    @property
    def unique_biz_no(self):
        return self._unique_biz_no

    @unique_biz_no.setter
    def unique_biz_no(self, value):
        self._unique_biz_no = value
    @property
    def used_times(self):
        return self._used_times

    @used_times.setter
    def used_times(self, value):
        self._used_times = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceServicerightsusageQueryResponse, self).parse_response_content(response_content)
        if 'available_stock' in response:
            self.available_stock = response['available_stock']
        if 'event_id' in response:
            self.event_id = response['event_id']
        if 'first_use_time' in response:
            self.first_use_time = response['first_use_time']
        if 'fulfillment_data' in response:
            self.fulfillment_data = response['fulfillment_data']
        if 'fulfillment_id' in response:
            self.fulfillment_id = response['fulfillment_id']
        if 'fulfillment_name' in response:
            self.fulfillment_name = response['fulfillment_name']
        if 'fulfillment_status' in response:
            self.fulfillment_status = response['fulfillment_status']
        if 'fulfillment_type' in response:
            self.fulfillment_type = response['fulfillment_type']
        if 'occur_time' in response:
            self.occur_time = response['occur_time']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_unique_biz_no' in response:
            self.out_unique_biz_no = response['out_unique_biz_no']
        if 'service_item_id' in response:
            self.service_item_id = response['service_item_id']
        if 'unique_biz_no' in response:
            self.unique_biz_no = response['unique_biz_no']
        if 'used_times' in response:
            self.used_times = response['used_times']
        if 'user_id' in response:
            self.user_id = response['user_id']
