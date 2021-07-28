#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TextInstance import TextInstance
from alipay.aop.api.domain.MaterialDetail import MaterialDetail
from alipay.aop.api.domain.CreativeRefuseExtendInfo import CreativeRefuseExtendInfo
from alipay.aop.api.domain.TextInstance import TextInstance
from alipay.aop.api.domain.MaterialDetail import MaterialDetail


class CreativeDetail(object):

    def __init__(self):
        self._action_type = None
        self._audit_order_id = None
        self._batch_tag = None
        self._click = None
        self._cost = None
        self._creative_id = None
        self._creative_outer_id = None
        self._desc_list = None
        self._extend_info = None
        self._group_outer_id = None
        self._img_list = None
        self._impression = None
        self._lbs_list = None
        self._name = None
        self._plan_outer_id = None
        self._principal_id = None
        self._refuse_extend_info = None
        self._refuse_reason = None
        self._region_list = None
        self._status = None
        self._store_id = None
        self._target_app_id = None
        self._target_url = None
        self._template_id = None
        self._title_list = None
        self._user_id = None
        self._video_list = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def audit_order_id(self):
        return self._audit_order_id

    @audit_order_id.setter
    def audit_order_id(self, value):
        self._audit_order_id = value
    @property
    def batch_tag(self):
        return self._batch_tag

    @batch_tag.setter
    def batch_tag(self, value):
        self._batch_tag = value
    @property
    def click(self):
        return self._click

    @click.setter
    def click(self, value):
        self._click = value
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value
    @property
    def creative_id(self):
        return self._creative_id

    @creative_id.setter
    def creative_id(self, value):
        self._creative_id = value
    @property
    def creative_outer_id(self):
        return self._creative_outer_id

    @creative_outer_id.setter
    def creative_outer_id(self, value):
        self._creative_outer_id = value
    @property
    def desc_list(self):
        return self._desc_list

    @desc_list.setter
    def desc_list(self, value):
        if isinstance(value, list):
            self._desc_list = list()
            for i in value:
                if isinstance(i, TextInstance):
                    self._desc_list.append(i)
                else:
                    self._desc_list.append(TextInstance.from_alipay_dict(i))
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def group_outer_id(self):
        return self._group_outer_id

    @group_outer_id.setter
    def group_outer_id(self, value):
        self._group_outer_id = value
    @property
    def img_list(self):
        return self._img_list

    @img_list.setter
    def img_list(self, value):
        if isinstance(value, list):
            self._img_list = list()
            for i in value:
                if isinstance(i, MaterialDetail):
                    self._img_list.append(i)
                else:
                    self._img_list.append(MaterialDetail.from_alipay_dict(i))
    @property
    def impression(self):
        return self._impression

    @impression.setter
    def impression(self, value):
        self._impression = value
    @property
    def lbs_list(self):
        return self._lbs_list

    @lbs_list.setter
    def lbs_list(self, value):
        if isinstance(value, list):
            self._lbs_list = list()
            for i in value:
                self._lbs_list.append(i)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def plan_outer_id(self):
        return self._plan_outer_id

    @plan_outer_id.setter
    def plan_outer_id(self, value):
        self._plan_outer_id = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def refuse_extend_info(self):
        return self._refuse_extend_info

    @refuse_extend_info.setter
    def refuse_extend_info(self, value):
        if isinstance(value, CreativeRefuseExtendInfo):
            self._refuse_extend_info = value
        else:
            self._refuse_extend_info = CreativeRefuseExtendInfo.from_alipay_dict(value)
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value
    @property
    def region_list(self):
        return self._region_list

    @region_list.setter
    def region_list(self, value):
        if isinstance(value, list):
            self._region_list = list()
            for i in value:
                self._region_list.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def target_app_id(self):
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, value):
        self._target_app_id = value
    @property
    def target_url(self):
        return self._target_url

    @target_url.setter
    def target_url(self, value):
        self._target_url = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def title_list(self):
        return self._title_list

    @title_list.setter
    def title_list(self, value):
        if isinstance(value, list):
            self._title_list = list()
            for i in value:
                if isinstance(i, TextInstance):
                    self._title_list.append(i)
                else:
                    self._title_list.append(TextInstance.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def video_list(self):
        return self._video_list

    @video_list.setter
    def video_list(self, value):
        if isinstance(value, list):
            self._video_list = list()
            for i in value:
                if isinstance(i, MaterialDetail):
                    self._video_list.append(i)
                else:
                    self._video_list.append(MaterialDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.audit_order_id:
            if hasattr(self.audit_order_id, 'to_alipay_dict'):
                params['audit_order_id'] = self.audit_order_id.to_alipay_dict()
            else:
                params['audit_order_id'] = self.audit_order_id
        if self.batch_tag:
            if hasattr(self.batch_tag, 'to_alipay_dict'):
                params['batch_tag'] = self.batch_tag.to_alipay_dict()
            else:
                params['batch_tag'] = self.batch_tag
        if self.click:
            if hasattr(self.click, 'to_alipay_dict'):
                params['click'] = self.click.to_alipay_dict()
            else:
                params['click'] = self.click
        if self.cost:
            if hasattr(self.cost, 'to_alipay_dict'):
                params['cost'] = self.cost.to_alipay_dict()
            else:
                params['cost'] = self.cost
        if self.creative_id:
            if hasattr(self.creative_id, 'to_alipay_dict'):
                params['creative_id'] = self.creative_id.to_alipay_dict()
            else:
                params['creative_id'] = self.creative_id
        if self.creative_outer_id:
            if hasattr(self.creative_outer_id, 'to_alipay_dict'):
                params['creative_outer_id'] = self.creative_outer_id.to_alipay_dict()
            else:
                params['creative_outer_id'] = self.creative_outer_id
        if self.desc_list:
            if isinstance(self.desc_list, list):
                for i in range(0, len(self.desc_list)):
                    element = self.desc_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.desc_list[i] = element.to_alipay_dict()
            if hasattr(self.desc_list, 'to_alipay_dict'):
                params['desc_list'] = self.desc_list.to_alipay_dict()
            else:
                params['desc_list'] = self.desc_list
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.group_outer_id:
            if hasattr(self.group_outer_id, 'to_alipay_dict'):
                params['group_outer_id'] = self.group_outer_id.to_alipay_dict()
            else:
                params['group_outer_id'] = self.group_outer_id
        if self.img_list:
            if isinstance(self.img_list, list):
                for i in range(0, len(self.img_list)):
                    element = self.img_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.img_list[i] = element.to_alipay_dict()
            if hasattr(self.img_list, 'to_alipay_dict'):
                params['img_list'] = self.img_list.to_alipay_dict()
            else:
                params['img_list'] = self.img_list
        if self.impression:
            if hasattr(self.impression, 'to_alipay_dict'):
                params['impression'] = self.impression.to_alipay_dict()
            else:
                params['impression'] = self.impression
        if self.lbs_list:
            if isinstance(self.lbs_list, list):
                for i in range(0, len(self.lbs_list)):
                    element = self.lbs_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.lbs_list[i] = element.to_alipay_dict()
            if hasattr(self.lbs_list, 'to_alipay_dict'):
                params['lbs_list'] = self.lbs_list.to_alipay_dict()
            else:
                params['lbs_list'] = self.lbs_list
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.plan_outer_id:
            if hasattr(self.plan_outer_id, 'to_alipay_dict'):
                params['plan_outer_id'] = self.plan_outer_id.to_alipay_dict()
            else:
                params['plan_outer_id'] = self.plan_outer_id
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.refuse_extend_info:
            if hasattr(self.refuse_extend_info, 'to_alipay_dict'):
                params['refuse_extend_info'] = self.refuse_extend_info.to_alipay_dict()
            else:
                params['refuse_extend_info'] = self.refuse_extend_info
        if self.refuse_reason:
            if hasattr(self.refuse_reason, 'to_alipay_dict'):
                params['refuse_reason'] = self.refuse_reason.to_alipay_dict()
            else:
                params['refuse_reason'] = self.refuse_reason
        if self.region_list:
            if isinstance(self.region_list, list):
                for i in range(0, len(self.region_list)):
                    element = self.region_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.region_list[i] = element.to_alipay_dict()
            if hasattr(self.region_list, 'to_alipay_dict'):
                params['region_list'] = self.region_list.to_alipay_dict()
            else:
                params['region_list'] = self.region_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.target_app_id:
            if hasattr(self.target_app_id, 'to_alipay_dict'):
                params['target_app_id'] = self.target_app_id.to_alipay_dict()
            else:
                params['target_app_id'] = self.target_app_id
        if self.target_url:
            if hasattr(self.target_url, 'to_alipay_dict'):
                params['target_url'] = self.target_url.to_alipay_dict()
            else:
                params['target_url'] = self.target_url
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.title_list:
            if isinstance(self.title_list, list):
                for i in range(0, len(self.title_list)):
                    element = self.title_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.title_list[i] = element.to_alipay_dict()
            if hasattr(self.title_list, 'to_alipay_dict'):
                params['title_list'] = self.title_list.to_alipay_dict()
            else:
                params['title_list'] = self.title_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.video_list:
            if isinstance(self.video_list, list):
                for i in range(0, len(self.video_list)):
                    element = self.video_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.video_list[i] = element.to_alipay_dict()
            if hasattr(self.video_list, 'to_alipay_dict'):
                params['video_list'] = self.video_list.to_alipay_dict()
            else:
                params['video_list'] = self.video_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativeDetail()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'audit_order_id' in d:
            o.audit_order_id = d['audit_order_id']
        if 'batch_tag' in d:
            o.batch_tag = d['batch_tag']
        if 'click' in d:
            o.click = d['click']
        if 'cost' in d:
            o.cost = d['cost']
        if 'creative_id' in d:
            o.creative_id = d['creative_id']
        if 'creative_outer_id' in d:
            o.creative_outer_id = d['creative_outer_id']
        if 'desc_list' in d:
            o.desc_list = d['desc_list']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'group_outer_id' in d:
            o.group_outer_id = d['group_outer_id']
        if 'img_list' in d:
            o.img_list = d['img_list']
        if 'impression' in d:
            o.impression = d['impression']
        if 'lbs_list' in d:
            o.lbs_list = d['lbs_list']
        if 'name' in d:
            o.name = d['name']
        if 'plan_outer_id' in d:
            o.plan_outer_id = d['plan_outer_id']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'refuse_extend_info' in d:
            o.refuse_extend_info = d['refuse_extend_info']
        if 'refuse_reason' in d:
            o.refuse_reason = d['refuse_reason']
        if 'region_list' in d:
            o.region_list = d['region_list']
        if 'status' in d:
            o.status = d['status']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'target_app_id' in d:
            o.target_app_id = d['target_app_id']
        if 'target_url' in d:
            o.target_url = d['target_url']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'title_list' in d:
            o.title_list = d['title_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'video_list' in d:
            o.video_list = d['video_list']
        return o


