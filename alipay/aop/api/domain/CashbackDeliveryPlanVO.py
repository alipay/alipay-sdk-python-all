#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CashbackDeliveryPlanVO(object):

    def __init__(self):
        self._banner_image = None
        self._banner_title = None
        self._biz_position_type = None
        self._brand_id = None
        self._brand_logo = None
        self._brand_name = None
        self._button_text = None
        self._campaign_code = None
        self._cashback_rate = None
        self._city_coverage_list = None
        self._city_coverage_type = None
        self._config_source = None
        self._config_status = None
        self._copy_audit_id = None
        self._crowd_coverage_type = None
        self._crowd_package_id = None
        self._delivery_form = None
        self._delivery_type = None
        self._end_time = None
        self._fatigue_control_config = None
        self._fund_config = None
        self._gift_desc = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._out_biz_id = None
        self._out_link = None
        self._out_link_type = None
        self._plan_name = None
        self._priority = None
        self._start_time = None
        self._sub_status = None
        self._white_list_user = None
        self._wujie_plan_id = None

    @property
    def banner_image(self):
        return self._banner_image

    @banner_image.setter
    def banner_image(self, value):
        self._banner_image = value
    @property
    def banner_title(self):
        return self._banner_title

    @banner_title.setter
    def banner_title(self, value):
        self._banner_title = value
    @property
    def biz_position_type(self):
        return self._biz_position_type

    @biz_position_type.setter
    def biz_position_type(self, value):
        self._biz_position_type = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def button_text(self):
        return self._button_text

    @button_text.setter
    def button_text(self, value):
        self._button_text = value
    @property
    def campaign_code(self):
        return self._campaign_code

    @campaign_code.setter
    def campaign_code(self, value):
        self._campaign_code = value
    @property
    def cashback_rate(self):
        return self._cashback_rate

    @cashback_rate.setter
    def cashback_rate(self, value):
        self._cashback_rate = value
    @property
    def city_coverage_list(self):
        return self._city_coverage_list

    @city_coverage_list.setter
    def city_coverage_list(self, value):
        self._city_coverage_list = value
    @property
    def city_coverage_type(self):
        return self._city_coverage_type

    @city_coverage_type.setter
    def city_coverage_type(self, value):
        self._city_coverage_type = value
    @property
    def config_source(self):
        return self._config_source

    @config_source.setter
    def config_source(self, value):
        self._config_source = value
    @property
    def config_status(self):
        return self._config_status

    @config_status.setter
    def config_status(self, value):
        self._config_status = value
    @property
    def copy_audit_id(self):
        return self._copy_audit_id

    @copy_audit_id.setter
    def copy_audit_id(self, value):
        self._copy_audit_id = value
    @property
    def crowd_coverage_type(self):
        return self._crowd_coverage_type

    @crowd_coverage_type.setter
    def crowd_coverage_type(self, value):
        self._crowd_coverage_type = value
    @property
    def crowd_package_id(self):
        return self._crowd_package_id

    @crowd_package_id.setter
    def crowd_package_id(self, value):
        self._crowd_package_id = value
    @property
    def delivery_form(self):
        return self._delivery_form

    @delivery_form.setter
    def delivery_form(self, value):
        self._delivery_form = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fatigue_control_config(self):
        return self._fatigue_control_config

    @fatigue_control_config.setter
    def fatigue_control_config(self, value):
        self._fatigue_control_config = value
    @property
    def fund_config(self):
        return self._fund_config

    @fund_config.setter
    def fund_config(self, value):
        self._fund_config = value
    @property
    def gift_desc(self):
        return self._gift_desc

    @gift_desc.setter
    def gift_desc(self, value):
        self._gift_desc = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def out_link(self):
        return self._out_link

    @out_link.setter
    def out_link(self, value):
        self._out_link = value
    @property
    def out_link_type(self):
        return self._out_link_type

    @out_link_type.setter
    def out_link_type(self, value):
        self._out_link_type = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value
    @property
    def white_list_user(self):
        return self._white_list_user

    @white_list_user.setter
    def white_list_user(self, value):
        self._white_list_user = value
    @property
    def wujie_plan_id(self):
        return self._wujie_plan_id

    @wujie_plan_id.setter
    def wujie_plan_id(self, value):
        self._wujie_plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.banner_image:
            if hasattr(self.banner_image, 'to_alipay_dict'):
                params['banner_image'] = self.banner_image.to_alipay_dict()
            else:
                params['banner_image'] = self.banner_image
        if self.banner_title:
            if hasattr(self.banner_title, 'to_alipay_dict'):
                params['banner_title'] = self.banner_title.to_alipay_dict()
            else:
                params['banner_title'] = self.banner_title
        if self.biz_position_type:
            if hasattr(self.biz_position_type, 'to_alipay_dict'):
                params['biz_position_type'] = self.biz_position_type.to_alipay_dict()
            else:
                params['biz_position_type'] = self.biz_position_type
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.button_text:
            if hasattr(self.button_text, 'to_alipay_dict'):
                params['button_text'] = self.button_text.to_alipay_dict()
            else:
                params['button_text'] = self.button_text
        if self.campaign_code:
            if hasattr(self.campaign_code, 'to_alipay_dict'):
                params['campaign_code'] = self.campaign_code.to_alipay_dict()
            else:
                params['campaign_code'] = self.campaign_code
        if self.cashback_rate:
            if hasattr(self.cashback_rate, 'to_alipay_dict'):
                params['cashback_rate'] = self.cashback_rate.to_alipay_dict()
            else:
                params['cashback_rate'] = self.cashback_rate
        if self.city_coverage_list:
            if hasattr(self.city_coverage_list, 'to_alipay_dict'):
                params['city_coverage_list'] = self.city_coverage_list.to_alipay_dict()
            else:
                params['city_coverage_list'] = self.city_coverage_list
        if self.city_coverage_type:
            if hasattr(self.city_coverage_type, 'to_alipay_dict'):
                params['city_coverage_type'] = self.city_coverage_type.to_alipay_dict()
            else:
                params['city_coverage_type'] = self.city_coverage_type
        if self.config_source:
            if hasattr(self.config_source, 'to_alipay_dict'):
                params['config_source'] = self.config_source.to_alipay_dict()
            else:
                params['config_source'] = self.config_source
        if self.config_status:
            if hasattr(self.config_status, 'to_alipay_dict'):
                params['config_status'] = self.config_status.to_alipay_dict()
            else:
                params['config_status'] = self.config_status
        if self.copy_audit_id:
            if hasattr(self.copy_audit_id, 'to_alipay_dict'):
                params['copy_audit_id'] = self.copy_audit_id.to_alipay_dict()
            else:
                params['copy_audit_id'] = self.copy_audit_id
        if self.crowd_coverage_type:
            if hasattr(self.crowd_coverage_type, 'to_alipay_dict'):
                params['crowd_coverage_type'] = self.crowd_coverage_type.to_alipay_dict()
            else:
                params['crowd_coverage_type'] = self.crowd_coverage_type
        if self.crowd_package_id:
            if hasattr(self.crowd_package_id, 'to_alipay_dict'):
                params['crowd_package_id'] = self.crowd_package_id.to_alipay_dict()
            else:
                params['crowd_package_id'] = self.crowd_package_id
        if self.delivery_form:
            if hasattr(self.delivery_form, 'to_alipay_dict'):
                params['delivery_form'] = self.delivery_form.to_alipay_dict()
            else:
                params['delivery_form'] = self.delivery_form
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.fatigue_control_config:
            if hasattr(self.fatigue_control_config, 'to_alipay_dict'):
                params['fatigue_control_config'] = self.fatigue_control_config.to_alipay_dict()
            else:
                params['fatigue_control_config'] = self.fatigue_control_config
        if self.fund_config:
            if hasattr(self.fund_config, 'to_alipay_dict'):
                params['fund_config'] = self.fund_config.to_alipay_dict()
            else:
                params['fund_config'] = self.fund_config
        if self.gift_desc:
            if hasattr(self.gift_desc, 'to_alipay_dict'):
                params['gift_desc'] = self.gift_desc.to_alipay_dict()
            else:
                params['gift_desc'] = self.gift_desc
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.out_link:
            if hasattr(self.out_link, 'to_alipay_dict'):
                params['out_link'] = self.out_link.to_alipay_dict()
            else:
                params['out_link'] = self.out_link
        if self.out_link_type:
            if hasattr(self.out_link_type, 'to_alipay_dict'):
                params['out_link_type'] = self.out_link_type.to_alipay_dict()
            else:
                params['out_link_type'] = self.out_link_type
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_status:
            if hasattr(self.sub_status, 'to_alipay_dict'):
                params['sub_status'] = self.sub_status.to_alipay_dict()
            else:
                params['sub_status'] = self.sub_status
        if self.white_list_user:
            if hasattr(self.white_list_user, 'to_alipay_dict'):
                params['white_list_user'] = self.white_list_user.to_alipay_dict()
            else:
                params['white_list_user'] = self.white_list_user
        if self.wujie_plan_id:
            if hasattr(self.wujie_plan_id, 'to_alipay_dict'):
                params['wujie_plan_id'] = self.wujie_plan_id.to_alipay_dict()
            else:
                params['wujie_plan_id'] = self.wujie_plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CashbackDeliveryPlanVO()
        if 'banner_image' in d:
            o.banner_image = d['banner_image']
        if 'banner_title' in d:
            o.banner_title = d['banner_title']
        if 'biz_position_type' in d:
            o.biz_position_type = d['biz_position_type']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'button_text' in d:
            o.button_text = d['button_text']
        if 'campaign_code' in d:
            o.campaign_code = d['campaign_code']
        if 'cashback_rate' in d:
            o.cashback_rate = d['cashback_rate']
        if 'city_coverage_list' in d:
            o.city_coverage_list = d['city_coverage_list']
        if 'city_coverage_type' in d:
            o.city_coverage_type = d['city_coverage_type']
        if 'config_source' in d:
            o.config_source = d['config_source']
        if 'config_status' in d:
            o.config_status = d['config_status']
        if 'copy_audit_id' in d:
            o.copy_audit_id = d['copy_audit_id']
        if 'crowd_coverage_type' in d:
            o.crowd_coverage_type = d['crowd_coverage_type']
        if 'crowd_package_id' in d:
            o.crowd_package_id = d['crowd_package_id']
        if 'delivery_form' in d:
            o.delivery_form = d['delivery_form']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fatigue_control_config' in d:
            o.fatigue_control_config = d['fatigue_control_config']
        if 'fund_config' in d:
            o.fund_config = d['fund_config']
        if 'gift_desc' in d:
            o.gift_desc = d['gift_desc']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'out_link' in d:
            o.out_link = d['out_link']
        if 'out_link_type' in d:
            o.out_link_type = d['out_link_type']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'priority' in d:
            o.priority = d['priority']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_status' in d:
            o.sub_status = d['sub_status']
        if 'white_list_user' in d:
            o.white_list_user = d['white_list_user']
        if 'wujie_plan_id' in d:
            o.wujie_plan_id = d['wujie_plan_id']
        return o


