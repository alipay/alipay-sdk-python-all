#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreativePageListRes(object):

    def __init__(self):
        self._ad_id = None
        self._ad_name = None
        self._creative_biz_status = None
        self._creative_type = None
        self._gmt_modified = None
        self._group_id = None
        self._group_name = None
        self._market_target_code = None
        self._market_target_name = None
        self._plan_id = None
        self._plan_name = None
        self._principal_id = None
        self._punish_reason = None
        self._risk_status = None
        self._scene_code = None
        self._status = None
        self._template_id = None

    @property
    def ad_id(self):
        return self._ad_id

    @ad_id.setter
    def ad_id(self, value):
        self._ad_id = value
    @property
    def ad_name(self):
        return self._ad_name

    @ad_name.setter
    def ad_name(self, value):
        self._ad_name = value
    @property
    def creative_biz_status(self):
        return self._creative_biz_status

    @creative_biz_status.setter
    def creative_biz_status(self, value):
        self._creative_biz_status = value
    @property
    def creative_type(self):
        return self._creative_type

    @creative_type.setter
    def creative_type(self, value):
        self._creative_type = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def market_target_code(self):
        return self._market_target_code

    @market_target_code.setter
    def market_target_code(self, value):
        self._market_target_code = value
    @property
    def market_target_name(self):
        return self._market_target_name

    @market_target_name.setter
    def market_target_name(self, value):
        self._market_target_name = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def punish_reason(self):
        return self._punish_reason

    @punish_reason.setter
    def punish_reason(self, value):
        self._punish_reason = value
    @property
    def risk_status(self):
        return self._risk_status

    @risk_status.setter
    def risk_status(self, value):
        self._risk_status = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_id:
            if hasattr(self.ad_id, 'to_alipay_dict'):
                params['ad_id'] = self.ad_id.to_alipay_dict()
            else:
                params['ad_id'] = self.ad_id
        if self.ad_name:
            if hasattr(self.ad_name, 'to_alipay_dict'):
                params['ad_name'] = self.ad_name.to_alipay_dict()
            else:
                params['ad_name'] = self.ad_name
        if self.creative_biz_status:
            if hasattr(self.creative_biz_status, 'to_alipay_dict'):
                params['creative_biz_status'] = self.creative_biz_status.to_alipay_dict()
            else:
                params['creative_biz_status'] = self.creative_biz_status
        if self.creative_type:
            if hasattr(self.creative_type, 'to_alipay_dict'):
                params['creative_type'] = self.creative_type.to_alipay_dict()
            else:
                params['creative_type'] = self.creative_type
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.market_target_code:
            if hasattr(self.market_target_code, 'to_alipay_dict'):
                params['market_target_code'] = self.market_target_code.to_alipay_dict()
            else:
                params['market_target_code'] = self.market_target_code
        if self.market_target_name:
            if hasattr(self.market_target_name, 'to_alipay_dict'):
                params['market_target_name'] = self.market_target_name.to_alipay_dict()
            else:
                params['market_target_name'] = self.market_target_name
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.punish_reason:
            if hasattr(self.punish_reason, 'to_alipay_dict'):
                params['punish_reason'] = self.punish_reason.to_alipay_dict()
            else:
                params['punish_reason'] = self.punish_reason
        if self.risk_status:
            if hasattr(self.risk_status, 'to_alipay_dict'):
                params['risk_status'] = self.risk_status.to_alipay_dict()
            else:
                params['risk_status'] = self.risk_status
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativePageListRes()
        if 'ad_id' in d:
            o.ad_id = d['ad_id']
        if 'ad_name' in d:
            o.ad_name = d['ad_name']
        if 'creative_biz_status' in d:
            o.creative_biz_status = d['creative_biz_status']
        if 'creative_type' in d:
            o.creative_type = d['creative_type']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'market_target_code' in d:
            o.market_target_code = d['market_target_code']
        if 'market_target_name' in d:
            o.market_target_name = d['market_target_name']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'punish_reason' in d:
            o.punish_reason = d['punish_reason']
        if 'risk_status' in d:
            o.risk_status = d['risk_status']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'status' in d:
            o.status = d['status']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


