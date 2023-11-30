#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RealAmountRatioIncentiveRule import RealAmountRatioIncentiveRule


class AlipayCommerceCommonTasktemplateCreateormodifyModel(object):

    def __init__(self):
        self._applet_id = None
        self._create_biz_no = None
        self._funder_id = None
        self._incentive_rule = None
        self._max_receive_num = None
        self._merchant_pid = None
        self._operate_open_id = None
        self._operate_user_id = None
        self._organizer_id = None
        self._organizer_name = None
        self._pre_content = None
        self._show_name = None
        self._show_picture = None
        self._show_public = None
        self._task_desc = None
        self._task_detail_url = None
        self._task_end_time = None
        self._task_name = None
        self._task_start_time = None
        self._task_template_id = None

    @property
    def applet_id(self):
        return self._applet_id

    @applet_id.setter
    def applet_id(self, value):
        self._applet_id = value
    @property
    def create_biz_no(self):
        return self._create_biz_no

    @create_biz_no.setter
    def create_biz_no(self, value):
        self._create_biz_no = value
    @property
    def funder_id(self):
        return self._funder_id

    @funder_id.setter
    def funder_id(self, value):
        self._funder_id = value
    @property
    def incentive_rule(self):
        return self._incentive_rule

    @incentive_rule.setter
    def incentive_rule(self, value):
        if isinstance(value, RealAmountRatioIncentiveRule):
            self._incentive_rule = value
        else:
            self._incentive_rule = RealAmountRatioIncentiveRule.from_alipay_dict(value)
    @property
    def max_receive_num(self):
        return self._max_receive_num

    @max_receive_num.setter
    def max_receive_num(self, value):
        self._max_receive_num = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def operate_open_id(self):
        return self._operate_open_id

    @operate_open_id.setter
    def operate_open_id(self, value):
        self._operate_open_id = value
    @property
    def operate_user_id(self):
        return self._operate_user_id

    @operate_user_id.setter
    def operate_user_id(self, value):
        self._operate_user_id = value
    @property
    def organizer_id(self):
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, value):
        self._organizer_id = value
    @property
    def organizer_name(self):
        return self._organizer_name

    @organizer_name.setter
    def organizer_name(self, value):
        self._organizer_name = value
    @property
    def pre_content(self):
        return self._pre_content

    @pre_content.setter
    def pre_content(self, value):
        self._pre_content = value
    @property
    def show_name(self):
        return self._show_name

    @show_name.setter
    def show_name(self, value):
        self._show_name = value
    @property
    def show_picture(self):
        return self._show_picture

    @show_picture.setter
    def show_picture(self, value):
        self._show_picture = value
    @property
    def show_public(self):
        return self._show_public

    @show_public.setter
    def show_public(self, value):
        self._show_public = value
    @property
    def task_desc(self):
        return self._task_desc

    @task_desc.setter
    def task_desc(self, value):
        self._task_desc = value
    @property
    def task_detail_url(self):
        return self._task_detail_url

    @task_detail_url.setter
    def task_detail_url(self, value):
        self._task_detail_url = value
    @property
    def task_end_time(self):
        return self._task_end_time

    @task_end_time.setter
    def task_end_time(self, value):
        self._task_end_time = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_start_time(self):
        return self._task_start_time

    @task_start_time.setter
    def task_start_time(self, value):
        self._task_start_time = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.applet_id:
            if hasattr(self.applet_id, 'to_alipay_dict'):
                params['applet_id'] = self.applet_id.to_alipay_dict()
            else:
                params['applet_id'] = self.applet_id
        if self.create_biz_no:
            if hasattr(self.create_biz_no, 'to_alipay_dict'):
                params['create_biz_no'] = self.create_biz_no.to_alipay_dict()
            else:
                params['create_biz_no'] = self.create_biz_no
        if self.funder_id:
            if hasattr(self.funder_id, 'to_alipay_dict'):
                params['funder_id'] = self.funder_id.to_alipay_dict()
            else:
                params['funder_id'] = self.funder_id
        if self.incentive_rule:
            if hasattr(self.incentive_rule, 'to_alipay_dict'):
                params['incentive_rule'] = self.incentive_rule.to_alipay_dict()
            else:
                params['incentive_rule'] = self.incentive_rule
        if self.max_receive_num:
            if hasattr(self.max_receive_num, 'to_alipay_dict'):
                params['max_receive_num'] = self.max_receive_num.to_alipay_dict()
            else:
                params['max_receive_num'] = self.max_receive_num
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.operate_open_id:
            if hasattr(self.operate_open_id, 'to_alipay_dict'):
                params['operate_open_id'] = self.operate_open_id.to_alipay_dict()
            else:
                params['operate_open_id'] = self.operate_open_id
        if self.operate_user_id:
            if hasattr(self.operate_user_id, 'to_alipay_dict'):
                params['operate_user_id'] = self.operate_user_id.to_alipay_dict()
            else:
                params['operate_user_id'] = self.operate_user_id
        if self.organizer_id:
            if hasattr(self.organizer_id, 'to_alipay_dict'):
                params['organizer_id'] = self.organizer_id.to_alipay_dict()
            else:
                params['organizer_id'] = self.organizer_id
        if self.organizer_name:
            if hasattr(self.organizer_name, 'to_alipay_dict'):
                params['organizer_name'] = self.organizer_name.to_alipay_dict()
            else:
                params['organizer_name'] = self.organizer_name
        if self.pre_content:
            if hasattr(self.pre_content, 'to_alipay_dict'):
                params['pre_content'] = self.pre_content.to_alipay_dict()
            else:
                params['pre_content'] = self.pre_content
        if self.show_name:
            if hasattr(self.show_name, 'to_alipay_dict'):
                params['show_name'] = self.show_name.to_alipay_dict()
            else:
                params['show_name'] = self.show_name
        if self.show_picture:
            if hasattr(self.show_picture, 'to_alipay_dict'):
                params['show_picture'] = self.show_picture.to_alipay_dict()
            else:
                params['show_picture'] = self.show_picture
        if self.show_public:
            if hasattr(self.show_public, 'to_alipay_dict'):
                params['show_public'] = self.show_public.to_alipay_dict()
            else:
                params['show_public'] = self.show_public
        if self.task_desc:
            if hasattr(self.task_desc, 'to_alipay_dict'):
                params['task_desc'] = self.task_desc.to_alipay_dict()
            else:
                params['task_desc'] = self.task_desc
        if self.task_detail_url:
            if hasattr(self.task_detail_url, 'to_alipay_dict'):
                params['task_detail_url'] = self.task_detail_url.to_alipay_dict()
            else:
                params['task_detail_url'] = self.task_detail_url
        if self.task_end_time:
            if hasattr(self.task_end_time, 'to_alipay_dict'):
                params['task_end_time'] = self.task_end_time.to_alipay_dict()
            else:
                params['task_end_time'] = self.task_end_time
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_start_time:
            if hasattr(self.task_start_time, 'to_alipay_dict'):
                params['task_start_time'] = self.task_start_time.to_alipay_dict()
            else:
                params['task_start_time'] = self.task_start_time
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommonTasktemplateCreateormodifyModel()
        if 'applet_id' in d:
            o.applet_id = d['applet_id']
        if 'create_biz_no' in d:
            o.create_biz_no = d['create_biz_no']
        if 'funder_id' in d:
            o.funder_id = d['funder_id']
        if 'incentive_rule' in d:
            o.incentive_rule = d['incentive_rule']
        if 'max_receive_num' in d:
            o.max_receive_num = d['max_receive_num']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'operate_open_id' in d:
            o.operate_open_id = d['operate_open_id']
        if 'operate_user_id' in d:
            o.operate_user_id = d['operate_user_id']
        if 'organizer_id' in d:
            o.organizer_id = d['organizer_id']
        if 'organizer_name' in d:
            o.organizer_name = d['organizer_name']
        if 'pre_content' in d:
            o.pre_content = d['pre_content']
        if 'show_name' in d:
            o.show_name = d['show_name']
        if 'show_picture' in d:
            o.show_picture = d['show_picture']
        if 'show_public' in d:
            o.show_public = d['show_public']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'task_detail_url' in d:
            o.task_detail_url = d['task_detail_url']
        if 'task_end_time' in d:
            o.task_end_time = d['task_end_time']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_start_time' in d:
            o.task_start_time = d['task_start_time']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        return o


