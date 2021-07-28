#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BPOpenApiTicket(object):

    def __init__(self):
        self._attachment = None
        self._biz_app = None
        self._biz_id = None
        self._business_context = None
        self._change_version = None
        self._config_id = None
        self._create_operator = None
        self._create_operator_name = None
        self._deal_url = None
        self._description = None
        self._detail_url = None
        self._display_name = None
        self._domain_id = None
        self._duration = None
        self._ext_property = None
        self._gmt_create = None
        self._gmt_end = None
        self._gmt_modified = None
        self._idempotent_id = None
        self._info_values = None
        self._instance_tnt_inst_id = None
        self._ip_role_id = None
        self._last_operate = None
        self._level = None
        self._modify_operator = None
        self._modify_operator_name = None
        self._name = None
        self._parent_ticket_id = None
        self._process_id = None
        self._should_finish_time = None
        self._state = None
        self._third_party = None
        self._tnt_inst_id = None
        self._wireless_detail_url = None

    @property
    def attachment(self):
        return self._attachment

    @attachment.setter
    def attachment(self, value):
        self._attachment = value
    @property
    def biz_app(self):
        return self._biz_app

    @biz_app.setter
    def biz_app(self, value):
        self._biz_app = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def business_context(self):
        return self._business_context

    @business_context.setter
    def business_context(self, value):
        self._business_context = value
    @property
    def change_version(self):
        return self._change_version

    @change_version.setter
    def change_version(self, value):
        self._change_version = value
    @property
    def config_id(self):
        return self._config_id

    @config_id.setter
    def config_id(self, value):
        self._config_id = value
    @property
    def create_operator(self):
        return self._create_operator

    @create_operator.setter
    def create_operator(self, value):
        self._create_operator = value
    @property
    def create_operator_name(self):
        return self._create_operator_name

    @create_operator_name.setter
    def create_operator_name(self, value):
        self._create_operator_name = value
    @property
    def deal_url(self):
        return self._deal_url

    @deal_url.setter
    def deal_url(self, value):
        self._deal_url = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def domain_id(self):
        return self._domain_id

    @domain_id.setter
    def domain_id(self, value):
        self._domain_id = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def ext_property(self):
        return self._ext_property

    @ext_property.setter
    def ext_property(self, value):
        self._ext_property = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def idempotent_id(self):
        return self._idempotent_id

    @idempotent_id.setter
    def idempotent_id(self, value):
        self._idempotent_id = value
    @property
    def info_values(self):
        return self._info_values

    @info_values.setter
    def info_values(self, value):
        if isinstance(value, list):
            self._info_values = list()
            for i in value:
                self._info_values.append(i)
    @property
    def instance_tnt_inst_id(self):
        return self._instance_tnt_inst_id

    @instance_tnt_inst_id.setter
    def instance_tnt_inst_id(self, value):
        self._instance_tnt_inst_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def last_operate(self):
        return self._last_operate

    @last_operate.setter
    def last_operate(self, value):
        self._last_operate = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def modify_operator(self):
        return self._modify_operator

    @modify_operator.setter
    def modify_operator(self, value):
        self._modify_operator = value
    @property
    def modify_operator_name(self):
        return self._modify_operator_name

    @modify_operator_name.setter
    def modify_operator_name(self, value):
        self._modify_operator_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def parent_ticket_id(self):
        return self._parent_ticket_id

    @parent_ticket_id.setter
    def parent_ticket_id(self, value):
        self._parent_ticket_id = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def should_finish_time(self):
        return self._should_finish_time

    @should_finish_time.setter
    def should_finish_time(self, value):
        self._should_finish_time = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def third_party(self):
        return self._third_party

    @third_party.setter
    def third_party(self, value):
        self._third_party = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def wireless_detail_url(self):
        return self._wireless_detail_url

    @wireless_detail_url.setter
    def wireless_detail_url(self, value):
        self._wireless_detail_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment:
            if hasattr(self.attachment, 'to_alipay_dict'):
                params['attachment'] = self.attachment.to_alipay_dict()
            else:
                params['attachment'] = self.attachment
        if self.biz_app:
            if hasattr(self.biz_app, 'to_alipay_dict'):
                params['biz_app'] = self.biz_app.to_alipay_dict()
            else:
                params['biz_app'] = self.biz_app
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.business_context:
            if hasattr(self.business_context, 'to_alipay_dict'):
                params['business_context'] = self.business_context.to_alipay_dict()
            else:
                params['business_context'] = self.business_context
        if self.change_version:
            if hasattr(self.change_version, 'to_alipay_dict'):
                params['change_version'] = self.change_version.to_alipay_dict()
            else:
                params['change_version'] = self.change_version
        if self.config_id:
            if hasattr(self.config_id, 'to_alipay_dict'):
                params['config_id'] = self.config_id.to_alipay_dict()
            else:
                params['config_id'] = self.config_id
        if self.create_operator:
            if hasattr(self.create_operator, 'to_alipay_dict'):
                params['create_operator'] = self.create_operator.to_alipay_dict()
            else:
                params['create_operator'] = self.create_operator
        if self.create_operator_name:
            if hasattr(self.create_operator_name, 'to_alipay_dict'):
                params['create_operator_name'] = self.create_operator_name.to_alipay_dict()
            else:
                params['create_operator_name'] = self.create_operator_name
        if self.deal_url:
            if hasattr(self.deal_url, 'to_alipay_dict'):
                params['deal_url'] = self.deal_url.to_alipay_dict()
            else:
                params['deal_url'] = self.deal_url
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.domain_id:
            if hasattr(self.domain_id, 'to_alipay_dict'):
                params['domain_id'] = self.domain_id.to_alipay_dict()
            else:
                params['domain_id'] = self.domain_id
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.ext_property:
            if hasattr(self.ext_property, 'to_alipay_dict'):
                params['ext_property'] = self.ext_property.to_alipay_dict()
            else:
                params['ext_property'] = self.ext_property
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.idempotent_id:
            if hasattr(self.idempotent_id, 'to_alipay_dict'):
                params['idempotent_id'] = self.idempotent_id.to_alipay_dict()
            else:
                params['idempotent_id'] = self.idempotent_id
        if self.info_values:
            if isinstance(self.info_values, list):
                for i in range(0, len(self.info_values)):
                    element = self.info_values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.info_values[i] = element.to_alipay_dict()
            if hasattr(self.info_values, 'to_alipay_dict'):
                params['info_values'] = self.info_values.to_alipay_dict()
            else:
                params['info_values'] = self.info_values
        if self.instance_tnt_inst_id:
            if hasattr(self.instance_tnt_inst_id, 'to_alipay_dict'):
                params['instance_tnt_inst_id'] = self.instance_tnt_inst_id.to_alipay_dict()
            else:
                params['instance_tnt_inst_id'] = self.instance_tnt_inst_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.last_operate:
            if hasattr(self.last_operate, 'to_alipay_dict'):
                params['last_operate'] = self.last_operate.to_alipay_dict()
            else:
                params['last_operate'] = self.last_operate
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.modify_operator:
            if hasattr(self.modify_operator, 'to_alipay_dict'):
                params['modify_operator'] = self.modify_operator.to_alipay_dict()
            else:
                params['modify_operator'] = self.modify_operator
        if self.modify_operator_name:
            if hasattr(self.modify_operator_name, 'to_alipay_dict'):
                params['modify_operator_name'] = self.modify_operator_name.to_alipay_dict()
            else:
                params['modify_operator_name'] = self.modify_operator_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.parent_ticket_id:
            if hasattr(self.parent_ticket_id, 'to_alipay_dict'):
                params['parent_ticket_id'] = self.parent_ticket_id.to_alipay_dict()
            else:
                params['parent_ticket_id'] = self.parent_ticket_id
        if self.process_id:
            if hasattr(self.process_id, 'to_alipay_dict'):
                params['process_id'] = self.process_id.to_alipay_dict()
            else:
                params['process_id'] = self.process_id
        if self.should_finish_time:
            if hasattr(self.should_finish_time, 'to_alipay_dict'):
                params['should_finish_time'] = self.should_finish_time.to_alipay_dict()
            else:
                params['should_finish_time'] = self.should_finish_time
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.third_party:
            if hasattr(self.third_party, 'to_alipay_dict'):
                params['third_party'] = self.third_party.to_alipay_dict()
            else:
                params['third_party'] = self.third_party
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.wireless_detail_url:
            if hasattr(self.wireless_detail_url, 'to_alipay_dict'):
                params['wireless_detail_url'] = self.wireless_detail_url.to_alipay_dict()
            else:
                params['wireless_detail_url'] = self.wireless_detail_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BPOpenApiTicket()
        if 'attachment' in d:
            o.attachment = d['attachment']
        if 'biz_app' in d:
            o.biz_app = d['biz_app']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'business_context' in d:
            o.business_context = d['business_context']
        if 'change_version' in d:
            o.change_version = d['change_version']
        if 'config_id' in d:
            o.config_id = d['config_id']
        if 'create_operator' in d:
            o.create_operator = d['create_operator']
        if 'create_operator_name' in d:
            o.create_operator_name = d['create_operator_name']
        if 'deal_url' in d:
            o.deal_url = d['deal_url']
        if 'description' in d:
            o.description = d['description']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'domain_id' in d:
            o.domain_id = d['domain_id']
        if 'duration' in d:
            o.duration = d['duration']
        if 'ext_property' in d:
            o.ext_property = d['ext_property']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'idempotent_id' in d:
            o.idempotent_id = d['idempotent_id']
        if 'info_values' in d:
            o.info_values = d['info_values']
        if 'instance_tnt_inst_id' in d:
            o.instance_tnt_inst_id = d['instance_tnt_inst_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'last_operate' in d:
            o.last_operate = d['last_operate']
        if 'level' in d:
            o.level = d['level']
        if 'modify_operator' in d:
            o.modify_operator = d['modify_operator']
        if 'modify_operator_name' in d:
            o.modify_operator_name = d['modify_operator_name']
        if 'name' in d:
            o.name = d['name']
        if 'parent_ticket_id' in d:
            o.parent_ticket_id = d['parent_ticket_id']
        if 'process_id' in d:
            o.process_id = d['process_id']
        if 'should_finish_time' in d:
            o.should_finish_time = d['should_finish_time']
        if 'state' in d:
            o.state = d['state']
        if 'third_party' in d:
            o.third_party = d['third_party']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'wireless_detail_url' in d:
            o.wireless_detail_url = d['wireless_detail_url']
        return o


