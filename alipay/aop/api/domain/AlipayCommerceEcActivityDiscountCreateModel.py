#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityBudgetInfo import ActivityBudgetInfo
from alipay.aop.api.domain.ActivityCrowdInfo import ActivityCrowdInfo
from alipay.aop.api.domain.ActivityPromotionInfo import ActivityPromotionInfo
from alipay.aop.api.domain.ActivityUserUsageLimitInfo import ActivityUserUsageLimitInfo


class AlipayCommerceEcActivityDiscountCreateModel(object):

    def __init__(self):
        self._activity_budget_info = None
        self._activity_crowd_info = None
        self._activity_description = None
        self._activity_name = None
        self._activity_promotion_info = None
        self._activity_user_usage_limit_info = None
        self._ant_shop_id = None
        self._end_date = None
        self._out_biz_no = None
        self._start_date = None

    @property
    def activity_budget_info(self):
        return self._activity_budget_info

    @activity_budget_info.setter
    def activity_budget_info(self, value):
        if isinstance(value, ActivityBudgetInfo):
            self._activity_budget_info = value
        else:
            self._activity_budget_info = ActivityBudgetInfo.from_alipay_dict(value)
    @property
    def activity_crowd_info(self):
        return self._activity_crowd_info

    @activity_crowd_info.setter
    def activity_crowd_info(self, value):
        if isinstance(value, ActivityCrowdInfo):
            self._activity_crowd_info = value
        else:
            self._activity_crowd_info = ActivityCrowdInfo.from_alipay_dict(value)
    @property
    def activity_description(self):
        return self._activity_description

    @activity_description.setter
    def activity_description(self, value):
        self._activity_description = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_promotion_info(self):
        return self._activity_promotion_info

    @activity_promotion_info.setter
    def activity_promotion_info(self, value):
        if isinstance(value, ActivityPromotionInfo):
            self._activity_promotion_info = value
        else:
            self._activity_promotion_info = ActivityPromotionInfo.from_alipay_dict(value)
    @property
    def activity_user_usage_limit_info(self):
        return self._activity_user_usage_limit_info

    @activity_user_usage_limit_info.setter
    def activity_user_usage_limit_info(self, value):
        if isinstance(value, ActivityUserUsageLimitInfo):
            self._activity_user_usage_limit_info = value
        else:
            self._activity_user_usage_limit_info = ActivityUserUsageLimitInfo.from_alipay_dict(value)
    @property
    def ant_shop_id(self):
        return self._ant_shop_id

    @ant_shop_id.setter
    def ant_shop_id(self, value):
        self._ant_shop_id = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_budget_info:
            if hasattr(self.activity_budget_info, 'to_alipay_dict'):
                params['activity_budget_info'] = self.activity_budget_info.to_alipay_dict()
            else:
                params['activity_budget_info'] = self.activity_budget_info
        if self.activity_crowd_info:
            if hasattr(self.activity_crowd_info, 'to_alipay_dict'):
                params['activity_crowd_info'] = self.activity_crowd_info.to_alipay_dict()
            else:
                params['activity_crowd_info'] = self.activity_crowd_info
        if self.activity_description:
            if hasattr(self.activity_description, 'to_alipay_dict'):
                params['activity_description'] = self.activity_description.to_alipay_dict()
            else:
                params['activity_description'] = self.activity_description
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_promotion_info:
            if hasattr(self.activity_promotion_info, 'to_alipay_dict'):
                params['activity_promotion_info'] = self.activity_promotion_info.to_alipay_dict()
            else:
                params['activity_promotion_info'] = self.activity_promotion_info
        if self.activity_user_usage_limit_info:
            if hasattr(self.activity_user_usage_limit_info, 'to_alipay_dict'):
                params['activity_user_usage_limit_info'] = self.activity_user_usage_limit_info.to_alipay_dict()
            else:
                params['activity_user_usage_limit_info'] = self.activity_user_usage_limit_info
        if self.ant_shop_id:
            if hasattr(self.ant_shop_id, 'to_alipay_dict'):
                params['ant_shop_id'] = self.ant_shop_id.to_alipay_dict()
            else:
                params['ant_shop_id'] = self.ant_shop_id
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcActivityDiscountCreateModel()
        if 'activity_budget_info' in d:
            o.activity_budget_info = d['activity_budget_info']
        if 'activity_crowd_info' in d:
            o.activity_crowd_info = d['activity_crowd_info']
        if 'activity_description' in d:
            o.activity_description = d['activity_description']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_promotion_info' in d:
            o.activity_promotion_info = d['activity_promotion_info']
        if 'activity_user_usage_limit_info' in d:
            o.activity_user_usage_limit_info = d['activity_user_usage_limit_info']
        if 'ant_shop_id' in d:
            o.ant_shop_id = d['ant_shop_id']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


