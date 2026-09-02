#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderExpoCheckconfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderExpoCheckconfigQueryResponse, self).__init__()
        self._activity_code = None
        self._activity_rule_button_name = None
        self._activity_rule_jump_type = None
        self._check_activity_delivery_channel = None
        self._check_template_type = None
        self._collection_name = None
        self._collection_type = None
        self._day_update_activity = None
        self._guide_image = None
        self._mall_id = None
        self._must_to_descrition = None
        self._open_pay_result_page = None
        self._open_share = None
        self._open_venue_exhibifion = None
        self._pay_result_page_action_url = None
        self._random_check_place = None
        self._rel_map = None
        self._rel_merchant_page = None
        self._service_provider_pid = None
        self._sync_service_provider = None
        self._title_image = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def activity_rule_button_name(self):
        return self._activity_rule_button_name

    @activity_rule_button_name.setter
    def activity_rule_button_name(self, value):
        self._activity_rule_button_name = value
    @property
    def activity_rule_jump_type(self):
        return self._activity_rule_jump_type

    @activity_rule_jump_type.setter
    def activity_rule_jump_type(self, value):
        self._activity_rule_jump_type = value
    @property
    def check_activity_delivery_channel(self):
        return self._check_activity_delivery_channel

    @check_activity_delivery_channel.setter
    def check_activity_delivery_channel(self, value):
        self._check_activity_delivery_channel = value
    @property
    def check_template_type(self):
        return self._check_template_type

    @check_template_type.setter
    def check_template_type(self, value):
        self._check_template_type = value
    @property
    def collection_name(self):
        return self._collection_name

    @collection_name.setter
    def collection_name(self, value):
        self._collection_name = value
    @property
    def collection_type(self):
        return self._collection_type

    @collection_type.setter
    def collection_type(self, value):
        self._collection_type = value
    @property
    def day_update_activity(self):
        return self._day_update_activity

    @day_update_activity.setter
    def day_update_activity(self, value):
        self._day_update_activity = value
    @property
    def guide_image(self):
        return self._guide_image

    @guide_image.setter
    def guide_image(self, value):
        self._guide_image = value
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def must_to_descrition(self):
        return self._must_to_descrition

    @must_to_descrition.setter
    def must_to_descrition(self, value):
        self._must_to_descrition = value
    @property
    def open_pay_result_page(self):
        return self._open_pay_result_page

    @open_pay_result_page.setter
    def open_pay_result_page(self, value):
        self._open_pay_result_page = value
    @property
    def open_share(self):
        return self._open_share

    @open_share.setter
    def open_share(self, value):
        self._open_share = value
    @property
    def open_venue_exhibifion(self):
        return self._open_venue_exhibifion

    @open_venue_exhibifion.setter
    def open_venue_exhibifion(self, value):
        self._open_venue_exhibifion = value
    @property
    def pay_result_page_action_url(self):
        return self._pay_result_page_action_url

    @pay_result_page_action_url.setter
    def pay_result_page_action_url(self, value):
        self._pay_result_page_action_url = value
    @property
    def random_check_place(self):
        return self._random_check_place

    @random_check_place.setter
    def random_check_place(self, value):
        self._random_check_place = value
    @property
    def rel_map(self):
        return self._rel_map

    @rel_map.setter
    def rel_map(self, value):
        self._rel_map = value
    @property
    def rel_merchant_page(self):
        return self._rel_merchant_page

    @rel_merchant_page.setter
    def rel_merchant_page(self, value):
        self._rel_merchant_page = value
    @property
    def service_provider_pid(self):
        return self._service_provider_pid

    @service_provider_pid.setter
    def service_provider_pid(self, value):
        self._service_provider_pid = value
    @property
    def sync_service_provider(self):
        return self._sync_service_provider

    @sync_service_provider.setter
    def sync_service_provider(self, value):
        self._sync_service_provider = value
    @property
    def title_image(self):
        return self._title_image

    @title_image.setter
    def title_image(self, value):
        self._title_image = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderExpoCheckconfigQueryResponse, self).parse_response_content(response_content)
        if 'activity_code' in response:
            self.activity_code = response['activity_code']
        if 'activity_rule_button_name' in response:
            self.activity_rule_button_name = response['activity_rule_button_name']
        if 'activity_rule_jump_type' in response:
            self.activity_rule_jump_type = response['activity_rule_jump_type']
        if 'check_activity_delivery_channel' in response:
            self.check_activity_delivery_channel = response['check_activity_delivery_channel']
        if 'check_template_type' in response:
            self.check_template_type = response['check_template_type']
        if 'collection_name' in response:
            self.collection_name = response['collection_name']
        if 'collection_type' in response:
            self.collection_type = response['collection_type']
        if 'day_update_activity' in response:
            self.day_update_activity = response['day_update_activity']
        if 'guide_image' in response:
            self.guide_image = response['guide_image']
        if 'mall_id' in response:
            self.mall_id = response['mall_id']
        if 'must_to_descrition' in response:
            self.must_to_descrition = response['must_to_descrition']
        if 'open_pay_result_page' in response:
            self.open_pay_result_page = response['open_pay_result_page']
        if 'open_share' in response:
            self.open_share = response['open_share']
        if 'open_venue_exhibifion' in response:
            self.open_venue_exhibifion = response['open_venue_exhibifion']
        if 'pay_result_page_action_url' in response:
            self.pay_result_page_action_url = response['pay_result_page_action_url']
        if 'random_check_place' in response:
            self.random_check_place = response['random_check_place']
        if 'rel_map' in response:
            self.rel_map = response['rel_map']
        if 'rel_merchant_page' in response:
            self.rel_merchant_page = response['rel_merchant_page']
        if 'service_provider_pid' in response:
            self.service_provider_pid = response['service_provider_pid']
        if 'sync_service_provider' in response:
            self.sync_service_provider = response['sync_service_provider']
        if 'title_image' in response:
            self.title_image = response['title_image']
