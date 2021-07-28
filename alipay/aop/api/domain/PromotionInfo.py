#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromotionInfo(object):

    def __init__(self):
        self._brand_name = None
        self._collected = None
        self._collected_count = None
        self._detail_url = None
        self._icon_url = None
        self._main_image_url = None
        self._out_prize_id = None
        self._promotion_id = None
        self._title = None
        self._using_condition = None
        self._using_scope = None
        self._valid_date_from = None
        self._valid_date_to = None
        self._valid_time_text = None
        self._voucher_usage_status = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def collected(self):
        return self._collected

    @collected.setter
    def collected(self, value):
        self._collected = value
    @property
    def collected_count(self):
        return self._collected_count

    @collected_count.setter
    def collected_count(self, value):
        self._collected_count = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value
    @property
    def main_image_url(self):
        return self._main_image_url

    @main_image_url.setter
    def main_image_url(self, value):
        self._main_image_url = value
    @property
    def out_prize_id(self):
        return self._out_prize_id

    @out_prize_id.setter
    def out_prize_id(self, value):
        self._out_prize_id = value
    @property
    def promotion_id(self):
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, value):
        self._promotion_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def using_condition(self):
        return self._using_condition

    @using_condition.setter
    def using_condition(self, value):
        self._using_condition = value
    @property
    def using_scope(self):
        return self._using_scope

    @using_scope.setter
    def using_scope(self, value):
        self._using_scope = value
    @property
    def valid_date_from(self):
        return self._valid_date_from

    @valid_date_from.setter
    def valid_date_from(self, value):
        self._valid_date_from = value
    @property
    def valid_date_to(self):
        return self._valid_date_to

    @valid_date_to.setter
    def valid_date_to(self, value):
        self._valid_date_to = value
    @property
    def valid_time_text(self):
        return self._valid_time_text

    @valid_time_text.setter
    def valid_time_text(self, value):
        self._valid_time_text = value
    @property
    def voucher_usage_status(self):
        return self._voucher_usage_status

    @voucher_usage_status.setter
    def voucher_usage_status(self, value):
        self._voucher_usage_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.collected:
            if hasattr(self.collected, 'to_alipay_dict'):
                params['collected'] = self.collected.to_alipay_dict()
            else:
                params['collected'] = self.collected
        if self.collected_count:
            if hasattr(self.collected_count, 'to_alipay_dict'):
                params['collected_count'] = self.collected_count.to_alipay_dict()
            else:
                params['collected_count'] = self.collected_count
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.icon_url:
            if hasattr(self.icon_url, 'to_alipay_dict'):
                params['icon_url'] = self.icon_url.to_alipay_dict()
            else:
                params['icon_url'] = self.icon_url
        if self.main_image_url:
            if hasattr(self.main_image_url, 'to_alipay_dict'):
                params['main_image_url'] = self.main_image_url.to_alipay_dict()
            else:
                params['main_image_url'] = self.main_image_url
        if self.out_prize_id:
            if hasattr(self.out_prize_id, 'to_alipay_dict'):
                params['out_prize_id'] = self.out_prize_id.to_alipay_dict()
            else:
                params['out_prize_id'] = self.out_prize_id
        if self.promotion_id:
            if hasattr(self.promotion_id, 'to_alipay_dict'):
                params['promotion_id'] = self.promotion_id.to_alipay_dict()
            else:
                params['promotion_id'] = self.promotion_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.using_condition:
            if hasattr(self.using_condition, 'to_alipay_dict'):
                params['using_condition'] = self.using_condition.to_alipay_dict()
            else:
                params['using_condition'] = self.using_condition
        if self.using_scope:
            if hasattr(self.using_scope, 'to_alipay_dict'):
                params['using_scope'] = self.using_scope.to_alipay_dict()
            else:
                params['using_scope'] = self.using_scope
        if self.valid_date_from:
            if hasattr(self.valid_date_from, 'to_alipay_dict'):
                params['valid_date_from'] = self.valid_date_from.to_alipay_dict()
            else:
                params['valid_date_from'] = self.valid_date_from
        if self.valid_date_to:
            if hasattr(self.valid_date_to, 'to_alipay_dict'):
                params['valid_date_to'] = self.valid_date_to.to_alipay_dict()
            else:
                params['valid_date_to'] = self.valid_date_to
        if self.valid_time_text:
            if hasattr(self.valid_time_text, 'to_alipay_dict'):
                params['valid_time_text'] = self.valid_time_text.to_alipay_dict()
            else:
                params['valid_time_text'] = self.valid_time_text
        if self.voucher_usage_status:
            if hasattr(self.voucher_usage_status, 'to_alipay_dict'):
                params['voucher_usage_status'] = self.voucher_usage_status.to_alipay_dict()
            else:
                params['voucher_usage_status'] = self.voucher_usage_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromotionInfo()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'collected' in d:
            o.collected = d['collected']
        if 'collected_count' in d:
            o.collected_count = d['collected_count']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'icon_url' in d:
            o.icon_url = d['icon_url']
        if 'main_image_url' in d:
            o.main_image_url = d['main_image_url']
        if 'out_prize_id' in d:
            o.out_prize_id = d['out_prize_id']
        if 'promotion_id' in d:
            o.promotion_id = d['promotion_id']
        if 'title' in d:
            o.title = d['title']
        if 'using_condition' in d:
            o.using_condition = d['using_condition']
        if 'using_scope' in d:
            o.using_scope = d['using_scope']
        if 'valid_date_from' in d:
            o.valid_date_from = d['valid_date_from']
        if 'valid_date_to' in d:
            o.valid_date_to = d['valid_date_to']
        if 'valid_time_text' in d:
            o.valid_time_text = d['valid_time_text']
        if 'voucher_usage_status' in d:
            o.voucher_usage_status = d['voucher_usage_status']
        return o


