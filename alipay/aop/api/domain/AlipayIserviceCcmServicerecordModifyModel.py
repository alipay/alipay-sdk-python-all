#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceRecordCatRequest import ServiceRecordCatRequest


class AlipayIserviceCcmServicerecordModifyModel(object):

    def __init__(self):
        self._acid = None
        self._aid = None
        self._ani = None
        self._asid = None
        self._category_list = None
        self._chat_begin_time = None
        self._chat_end_time = None
        self._city = None
        self._creator_id = None
        self._discon_symbol = None
        self._dnis = None
        self._file_size = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._memo = None
        self._modifier_id = None
        self._outbound_task_id = None
        self._satisfaction = None
        self._satisfaction_memo = None
        self._service_source = None
        self._service_time = None
        self._skillgroup_id = None
        self._skillgroup_name = None
        self._status = None
        self._tnt_inst_id = None
        self._user_id = None
        self._verify_result = None

    @property
    def acid(self):
        return self._acid

    @acid.setter
    def acid(self, value):
        self._acid = value
    @property
    def aid(self):
        return self._aid

    @aid.setter
    def aid(self, value):
        self._aid = value
    @property
    def ani(self):
        return self._ani

    @ani.setter
    def ani(self, value):
        self._ani = value
    @property
    def asid(self):
        return self._asid

    @asid.setter
    def asid(self, value):
        self._asid = value
    @property
    def category_list(self):
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        if isinstance(value, ServiceRecordCatRequest):
            self._category_list = value
        else:
            self._category_list = ServiceRecordCatRequest.from_alipay_dict(value)
    @property
    def chat_begin_time(self):
        return self._chat_begin_time

    @chat_begin_time.setter
    def chat_begin_time(self, value):
        self._chat_begin_time = value
    @property
    def chat_end_time(self):
        return self._chat_end_time

    @chat_end_time.setter
    def chat_end_time(self, value):
        self._chat_end_time = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def discon_symbol(self):
        return self._discon_symbol

    @discon_symbol.setter
    def discon_symbol(self, value):
        self._discon_symbol = value
    @property
    def dnis(self):
        return self._dnis

    @dnis.setter
    def dnis(self, value):
        self._dnis = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
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
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def modifier_id(self):
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, value):
        self._modifier_id = value
    @property
    def outbound_task_id(self):
        return self._outbound_task_id

    @outbound_task_id.setter
    def outbound_task_id(self, value):
        self._outbound_task_id = value
    @property
    def satisfaction(self):
        return self._satisfaction

    @satisfaction.setter
    def satisfaction(self, value):
        self._satisfaction = value
    @property
    def satisfaction_memo(self):
        return self._satisfaction_memo

    @satisfaction_memo.setter
    def satisfaction_memo(self, value):
        self._satisfaction_memo = value
    @property
    def service_source(self):
        return self._service_source

    @service_source.setter
    def service_source(self, value):
        self._service_source = value
    @property
    def service_time(self):
        return self._service_time

    @service_time.setter
    def service_time(self, value):
        self._service_time = value
    @property
    def skillgroup_id(self):
        return self._skillgroup_id

    @skillgroup_id.setter
    def skillgroup_id(self, value):
        self._skillgroup_id = value
    @property
    def skillgroup_name(self):
        return self._skillgroup_name

    @skillgroup_name.setter
    def skillgroup_name(self, value):
        self._skillgroup_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def verify_result(self):
        return self._verify_result

    @verify_result.setter
    def verify_result(self, value):
        self._verify_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.acid:
            if hasattr(self.acid, 'to_alipay_dict'):
                params['acid'] = self.acid.to_alipay_dict()
            else:
                params['acid'] = self.acid
        if self.aid:
            if hasattr(self.aid, 'to_alipay_dict'):
                params['aid'] = self.aid.to_alipay_dict()
            else:
                params['aid'] = self.aid
        if self.ani:
            if hasattr(self.ani, 'to_alipay_dict'):
                params['ani'] = self.ani.to_alipay_dict()
            else:
                params['ani'] = self.ani
        if self.asid:
            if hasattr(self.asid, 'to_alipay_dict'):
                params['asid'] = self.asid.to_alipay_dict()
            else:
                params['asid'] = self.asid
        if self.category_list:
            if hasattr(self.category_list, 'to_alipay_dict'):
                params['category_list'] = self.category_list.to_alipay_dict()
            else:
                params['category_list'] = self.category_list
        if self.chat_begin_time:
            if hasattr(self.chat_begin_time, 'to_alipay_dict'):
                params['chat_begin_time'] = self.chat_begin_time.to_alipay_dict()
            else:
                params['chat_begin_time'] = self.chat_begin_time
        if self.chat_end_time:
            if hasattr(self.chat_end_time, 'to_alipay_dict'):
                params['chat_end_time'] = self.chat_end_time.to_alipay_dict()
            else:
                params['chat_end_time'] = self.chat_end_time
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.discon_symbol:
            if hasattr(self.discon_symbol, 'to_alipay_dict'):
                params['discon_symbol'] = self.discon_symbol.to_alipay_dict()
            else:
                params['discon_symbol'] = self.discon_symbol
        if self.dnis:
            if hasattr(self.dnis, 'to_alipay_dict'):
                params['dnis'] = self.dnis.to_alipay_dict()
            else:
                params['dnis'] = self.dnis
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = self.file_size.to_alipay_dict()
            else:
                params['file_size'] = self.file_size
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
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.modifier_id:
            if hasattr(self.modifier_id, 'to_alipay_dict'):
                params['modifier_id'] = self.modifier_id.to_alipay_dict()
            else:
                params['modifier_id'] = self.modifier_id
        if self.outbound_task_id:
            if hasattr(self.outbound_task_id, 'to_alipay_dict'):
                params['outbound_task_id'] = self.outbound_task_id.to_alipay_dict()
            else:
                params['outbound_task_id'] = self.outbound_task_id
        if self.satisfaction:
            if hasattr(self.satisfaction, 'to_alipay_dict'):
                params['satisfaction'] = self.satisfaction.to_alipay_dict()
            else:
                params['satisfaction'] = self.satisfaction
        if self.satisfaction_memo:
            if hasattr(self.satisfaction_memo, 'to_alipay_dict'):
                params['satisfaction_memo'] = self.satisfaction_memo.to_alipay_dict()
            else:
                params['satisfaction_memo'] = self.satisfaction_memo
        if self.service_source:
            if hasattr(self.service_source, 'to_alipay_dict'):
                params['service_source'] = self.service_source.to_alipay_dict()
            else:
                params['service_source'] = self.service_source
        if self.service_time:
            if hasattr(self.service_time, 'to_alipay_dict'):
                params['service_time'] = self.service_time.to_alipay_dict()
            else:
                params['service_time'] = self.service_time
        if self.skillgroup_id:
            if hasattr(self.skillgroup_id, 'to_alipay_dict'):
                params['skillgroup_id'] = self.skillgroup_id.to_alipay_dict()
            else:
                params['skillgroup_id'] = self.skillgroup_id
        if self.skillgroup_name:
            if hasattr(self.skillgroup_name, 'to_alipay_dict'):
                params['skillgroup_name'] = self.skillgroup_name.to_alipay_dict()
            else:
                params['skillgroup_name'] = self.skillgroup_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.verify_result:
            if hasattr(self.verify_result, 'to_alipay_dict'):
                params['verify_result'] = self.verify_result.to_alipay_dict()
            else:
                params['verify_result'] = self.verify_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmServicerecordModifyModel()
        if 'acid' in d:
            o.acid = d['acid']
        if 'aid' in d:
            o.aid = d['aid']
        if 'ani' in d:
            o.ani = d['ani']
        if 'asid' in d:
            o.asid = d['asid']
        if 'category_list' in d:
            o.category_list = d['category_list']
        if 'chat_begin_time' in d:
            o.chat_begin_time = d['chat_begin_time']
        if 'chat_end_time' in d:
            o.chat_end_time = d['chat_end_time']
        if 'city' in d:
            o.city = d['city']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'discon_symbol' in d:
            o.discon_symbol = d['discon_symbol']
        if 'dnis' in d:
            o.dnis = d['dnis']
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'modifier_id' in d:
            o.modifier_id = d['modifier_id']
        if 'outbound_task_id' in d:
            o.outbound_task_id = d['outbound_task_id']
        if 'satisfaction' in d:
            o.satisfaction = d['satisfaction']
        if 'satisfaction_memo' in d:
            o.satisfaction_memo = d['satisfaction_memo']
        if 'service_source' in d:
            o.service_source = d['service_source']
        if 'service_time' in d:
            o.service_time = d['service_time']
        if 'skillgroup_id' in d:
            o.skillgroup_id = d['skillgroup_id']
        if 'skillgroup_name' in d:
            o.skillgroup_name = d['skillgroup_name']
        if 'status' in d:
            o.status = d['status']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'verify_result' in d:
            o.verify_result = d['verify_result']
        return o


