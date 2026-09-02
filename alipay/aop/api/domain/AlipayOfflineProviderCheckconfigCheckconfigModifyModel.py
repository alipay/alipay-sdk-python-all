#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderCheckconfigCheckconfigModifyModel(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.activity_rule_button_name:
            if hasattr(self.activity_rule_button_name, 'to_alipay_dict'):
                params['activity_rule_button_name'] = self.activity_rule_button_name.to_alipay_dict()
            else:
                params['activity_rule_button_name'] = self.activity_rule_button_name
        if self.activity_rule_jump_type:
            if hasattr(self.activity_rule_jump_type, 'to_alipay_dict'):
                params['activity_rule_jump_type'] = self.activity_rule_jump_type.to_alipay_dict()
            else:
                params['activity_rule_jump_type'] = self.activity_rule_jump_type
        if self.check_activity_delivery_channel:
            if hasattr(self.check_activity_delivery_channel, 'to_alipay_dict'):
                params['check_activity_delivery_channel'] = self.check_activity_delivery_channel.to_alipay_dict()
            else:
                params['check_activity_delivery_channel'] = self.check_activity_delivery_channel
        if self.check_template_type:
            if hasattr(self.check_template_type, 'to_alipay_dict'):
                params['check_template_type'] = self.check_template_type.to_alipay_dict()
            else:
                params['check_template_type'] = self.check_template_type
        if self.collection_name:
            if hasattr(self.collection_name, 'to_alipay_dict'):
                params['collection_name'] = self.collection_name.to_alipay_dict()
            else:
                params['collection_name'] = self.collection_name
        if self.collection_type:
            if hasattr(self.collection_type, 'to_alipay_dict'):
                params['collection_type'] = self.collection_type.to_alipay_dict()
            else:
                params['collection_type'] = self.collection_type
        if self.day_update_activity:
            if hasattr(self.day_update_activity, 'to_alipay_dict'):
                params['day_update_activity'] = self.day_update_activity.to_alipay_dict()
            else:
                params['day_update_activity'] = self.day_update_activity
        if self.guide_image:
            if hasattr(self.guide_image, 'to_alipay_dict'):
                params['guide_image'] = self.guide_image.to_alipay_dict()
            else:
                params['guide_image'] = self.guide_image
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.must_to_descrition:
            if hasattr(self.must_to_descrition, 'to_alipay_dict'):
                params['must_to_descrition'] = self.must_to_descrition.to_alipay_dict()
            else:
                params['must_to_descrition'] = self.must_to_descrition
        if self.open_pay_result_page:
            if hasattr(self.open_pay_result_page, 'to_alipay_dict'):
                params['open_pay_result_page'] = self.open_pay_result_page.to_alipay_dict()
            else:
                params['open_pay_result_page'] = self.open_pay_result_page
        if self.open_share:
            if hasattr(self.open_share, 'to_alipay_dict'):
                params['open_share'] = self.open_share.to_alipay_dict()
            else:
                params['open_share'] = self.open_share
        if self.open_venue_exhibifion:
            if hasattr(self.open_venue_exhibifion, 'to_alipay_dict'):
                params['open_venue_exhibifion'] = self.open_venue_exhibifion.to_alipay_dict()
            else:
                params['open_venue_exhibifion'] = self.open_venue_exhibifion
        if self.pay_result_page_action_url:
            if hasattr(self.pay_result_page_action_url, 'to_alipay_dict'):
                params['pay_result_page_action_url'] = self.pay_result_page_action_url.to_alipay_dict()
            else:
                params['pay_result_page_action_url'] = self.pay_result_page_action_url
        if self.random_check_place:
            if hasattr(self.random_check_place, 'to_alipay_dict'):
                params['random_check_place'] = self.random_check_place.to_alipay_dict()
            else:
                params['random_check_place'] = self.random_check_place
        if self.rel_map:
            if hasattr(self.rel_map, 'to_alipay_dict'):
                params['rel_map'] = self.rel_map.to_alipay_dict()
            else:
                params['rel_map'] = self.rel_map
        if self.rel_merchant_page:
            if hasattr(self.rel_merchant_page, 'to_alipay_dict'):
                params['rel_merchant_page'] = self.rel_merchant_page.to_alipay_dict()
            else:
                params['rel_merchant_page'] = self.rel_merchant_page
        if self.service_provider_pid:
            if hasattr(self.service_provider_pid, 'to_alipay_dict'):
                params['service_provider_pid'] = self.service_provider_pid.to_alipay_dict()
            else:
                params['service_provider_pid'] = self.service_provider_pid
        if self.sync_service_provider:
            if hasattr(self.sync_service_provider, 'to_alipay_dict'):
                params['sync_service_provider'] = self.sync_service_provider.to_alipay_dict()
            else:
                params['sync_service_provider'] = self.sync_service_provider
        if self.title_image:
            if hasattr(self.title_image, 'to_alipay_dict'):
                params['title_image'] = self.title_image.to_alipay_dict()
            else:
                params['title_image'] = self.title_image
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderCheckconfigCheckconfigModifyModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'activity_rule_button_name' in d:
            o.activity_rule_button_name = d['activity_rule_button_name']
        if 'activity_rule_jump_type' in d:
            o.activity_rule_jump_type = d['activity_rule_jump_type']
        if 'check_activity_delivery_channel' in d:
            o.check_activity_delivery_channel = d['check_activity_delivery_channel']
        if 'check_template_type' in d:
            o.check_template_type = d['check_template_type']
        if 'collection_name' in d:
            o.collection_name = d['collection_name']
        if 'collection_type' in d:
            o.collection_type = d['collection_type']
        if 'day_update_activity' in d:
            o.day_update_activity = d['day_update_activity']
        if 'guide_image' in d:
            o.guide_image = d['guide_image']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'must_to_descrition' in d:
            o.must_to_descrition = d['must_to_descrition']
        if 'open_pay_result_page' in d:
            o.open_pay_result_page = d['open_pay_result_page']
        if 'open_share' in d:
            o.open_share = d['open_share']
        if 'open_venue_exhibifion' in d:
            o.open_venue_exhibifion = d['open_venue_exhibifion']
        if 'pay_result_page_action_url' in d:
            o.pay_result_page_action_url = d['pay_result_page_action_url']
        if 'random_check_place' in d:
            o.random_check_place = d['random_check_place']
        if 'rel_map' in d:
            o.rel_map = d['rel_map']
        if 'rel_merchant_page' in d:
            o.rel_merchant_page = d['rel_merchant_page']
        if 'service_provider_pid' in d:
            o.service_provider_pid = d['service_provider_pid']
        if 'sync_service_provider' in d:
            o.sync_service_provider = d['sync_service_provider']
        if 'title_image' in d:
            o.title_image = d['title_image']
        return o


