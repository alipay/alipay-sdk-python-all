#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelPutPlanDTO(object):

    def __init__(self):
        self._activity_page = None
        self._bill_way = None
        self._channel_biz_id = None
        self._channel_biz_id_str = None
        self._channel_categorychannel_category = None
        self._channel_id = None
        self._creator_id = None
        self._creator_name = None
        self._crowd_ids = None
        self._customize_page = None
        self._exc_end_time = None
        self._exc_start_time = None
        self._exception_reason = None
        self._gmt_create = None
        self._gmt_modified = None
        self._gmt_plan_end = None
        self._gmt_plan_start = None
        self._id = None
        self._modifier_id = None
        self._modifier_name = None
        self._name = None
        self._page_type = None
        self._plan_content = None
        self._plan_source = None
        self._reject_reason = None
        self._repeat_times = None
        self._status = None
        self._tenant_code = None

    @property
    def activity_page(self):
        return self._activity_page

    @activity_page.setter
    def activity_page(self, value):
        self._activity_page = value
    @property
    def bill_way(self):
        return self._bill_way

    @bill_way.setter
    def bill_way(self, value):
        self._bill_way = value
    @property
    def channel_biz_id(self):
        return self._channel_biz_id

    @channel_biz_id.setter
    def channel_biz_id(self, value):
        self._channel_biz_id = value
    @property
    def channel_biz_id_str(self):
        return self._channel_biz_id_str

    @channel_biz_id_str.setter
    def channel_biz_id_str(self, value):
        self._channel_biz_id_str = value
    @property
    def channel_categorychannel_category(self):
        return self._channel_categorychannel_category

    @channel_categorychannel_category.setter
    def channel_categorychannel_category(self, value):
        self._channel_categorychannel_category = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def creator_name(self):
        return self._creator_name

    @creator_name.setter
    def creator_name(self, value):
        self._creator_name = value
    @property
    def crowd_ids(self):
        return self._crowd_ids

    @crowd_ids.setter
    def crowd_ids(self, value):
        self._crowd_ids = value
    @property
    def customize_page(self):
        return self._customize_page

    @customize_page.setter
    def customize_page(self, value):
        self._customize_page = value
    @property
    def exc_end_time(self):
        return self._exc_end_time

    @exc_end_time.setter
    def exc_end_time(self, value):
        self._exc_end_time = value
    @property
    def exc_start_time(self):
        return self._exc_start_time

    @exc_start_time.setter
    def exc_start_time(self, value):
        self._exc_start_time = value
    @property
    def exception_reason(self):
        return self._exception_reason

    @exception_reason.setter
    def exception_reason(self, value):
        self._exception_reason = value
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
    def gmt_plan_end(self):
        return self._gmt_plan_end

    @gmt_plan_end.setter
    def gmt_plan_end(self, value):
        self._gmt_plan_end = value
    @property
    def gmt_plan_start(self):
        return self._gmt_plan_start

    @gmt_plan_start.setter
    def gmt_plan_start(self, value):
        self._gmt_plan_start = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def modifier_id(self):
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, value):
        self._modifier_id = value
    @property
    def modifier_name(self):
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, value):
        self._modifier_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def page_type(self):
        return self._page_type

    @page_type.setter
    def page_type(self, value):
        self._page_type = value
    @property
    def plan_content(self):
        return self._plan_content

    @plan_content.setter
    def plan_content(self, value):
        self._plan_content = value
    @property
    def plan_source(self):
        return self._plan_source

    @plan_source.setter
    def plan_source(self, value):
        self._plan_source = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def repeat_times(self):
        return self._repeat_times

    @repeat_times.setter
    def repeat_times(self, value):
        self._repeat_times = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_page:
            if hasattr(self.activity_page, 'to_alipay_dict'):
                params['activity_page'] = self.activity_page.to_alipay_dict()
            else:
                params['activity_page'] = self.activity_page
        if self.bill_way:
            if hasattr(self.bill_way, 'to_alipay_dict'):
                params['bill_way'] = self.bill_way.to_alipay_dict()
            else:
                params['bill_way'] = self.bill_way
        if self.channel_biz_id:
            if hasattr(self.channel_biz_id, 'to_alipay_dict'):
                params['channel_biz_id'] = self.channel_biz_id.to_alipay_dict()
            else:
                params['channel_biz_id'] = self.channel_biz_id
        if self.channel_biz_id_str:
            if hasattr(self.channel_biz_id_str, 'to_alipay_dict'):
                params['channel_biz_id_str'] = self.channel_biz_id_str.to_alipay_dict()
            else:
                params['channel_biz_id_str'] = self.channel_biz_id_str
        if self.channel_categorychannel_category:
            if hasattr(self.channel_categorychannel_category, 'to_alipay_dict'):
                params['channel_categorychannel_category'] = self.channel_categorychannel_category.to_alipay_dict()
            else:
                params['channel_categorychannel_category'] = self.channel_categorychannel_category
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.creator_name:
            if hasattr(self.creator_name, 'to_alipay_dict'):
                params['creator_name'] = self.creator_name.to_alipay_dict()
            else:
                params['creator_name'] = self.creator_name
        if self.crowd_ids:
            if hasattr(self.crowd_ids, 'to_alipay_dict'):
                params['crowd_ids'] = self.crowd_ids.to_alipay_dict()
            else:
                params['crowd_ids'] = self.crowd_ids
        if self.customize_page:
            if hasattr(self.customize_page, 'to_alipay_dict'):
                params['customize_page'] = self.customize_page.to_alipay_dict()
            else:
                params['customize_page'] = self.customize_page
        if self.exc_end_time:
            if hasattr(self.exc_end_time, 'to_alipay_dict'):
                params['exc_end_time'] = self.exc_end_time.to_alipay_dict()
            else:
                params['exc_end_time'] = self.exc_end_time
        if self.exc_start_time:
            if hasattr(self.exc_start_time, 'to_alipay_dict'):
                params['exc_start_time'] = self.exc_start_time.to_alipay_dict()
            else:
                params['exc_start_time'] = self.exc_start_time
        if self.exception_reason:
            if hasattr(self.exception_reason, 'to_alipay_dict'):
                params['exception_reason'] = self.exception_reason.to_alipay_dict()
            else:
                params['exception_reason'] = self.exception_reason
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
        if self.gmt_plan_end:
            if hasattr(self.gmt_plan_end, 'to_alipay_dict'):
                params['gmt_plan_end'] = self.gmt_plan_end.to_alipay_dict()
            else:
                params['gmt_plan_end'] = self.gmt_plan_end
        if self.gmt_plan_start:
            if hasattr(self.gmt_plan_start, 'to_alipay_dict'):
                params['gmt_plan_start'] = self.gmt_plan_start.to_alipay_dict()
            else:
                params['gmt_plan_start'] = self.gmt_plan_start
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.modifier_id:
            if hasattr(self.modifier_id, 'to_alipay_dict'):
                params['modifier_id'] = self.modifier_id.to_alipay_dict()
            else:
                params['modifier_id'] = self.modifier_id
        if self.modifier_name:
            if hasattr(self.modifier_name, 'to_alipay_dict'):
                params['modifier_name'] = self.modifier_name.to_alipay_dict()
            else:
                params['modifier_name'] = self.modifier_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.page_type:
            if hasattr(self.page_type, 'to_alipay_dict'):
                params['page_type'] = self.page_type.to_alipay_dict()
            else:
                params['page_type'] = self.page_type
        if self.plan_content:
            if hasattr(self.plan_content, 'to_alipay_dict'):
                params['plan_content'] = self.plan_content.to_alipay_dict()
            else:
                params['plan_content'] = self.plan_content
        if self.plan_source:
            if hasattr(self.plan_source, 'to_alipay_dict'):
                params['plan_source'] = self.plan_source.to_alipay_dict()
            else:
                params['plan_source'] = self.plan_source
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.repeat_times:
            if hasattr(self.repeat_times, 'to_alipay_dict'):
                params['repeat_times'] = self.repeat_times.to_alipay_dict()
            else:
                params['repeat_times'] = self.repeat_times
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelPutPlanDTO()
        if 'activity_page' in d:
            o.activity_page = d['activity_page']
        if 'bill_way' in d:
            o.bill_way = d['bill_way']
        if 'channel_biz_id' in d:
            o.channel_biz_id = d['channel_biz_id']
        if 'channel_biz_id_str' in d:
            o.channel_biz_id_str = d['channel_biz_id_str']
        if 'channel_categorychannel_category' in d:
            o.channel_categorychannel_category = d['channel_categorychannel_category']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'creator_name' in d:
            o.creator_name = d['creator_name']
        if 'crowd_ids' in d:
            o.crowd_ids = d['crowd_ids']
        if 'customize_page' in d:
            o.customize_page = d['customize_page']
        if 'exc_end_time' in d:
            o.exc_end_time = d['exc_end_time']
        if 'exc_start_time' in d:
            o.exc_start_time = d['exc_start_time']
        if 'exception_reason' in d:
            o.exception_reason = d['exception_reason']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'gmt_plan_end' in d:
            o.gmt_plan_end = d['gmt_plan_end']
        if 'gmt_plan_start' in d:
            o.gmt_plan_start = d['gmt_plan_start']
        if 'id' in d:
            o.id = d['id']
        if 'modifier_id' in d:
            o.modifier_id = d['modifier_id']
        if 'modifier_name' in d:
            o.modifier_name = d['modifier_name']
        if 'name' in d:
            o.name = d['name']
        if 'page_type' in d:
            o.page_type = d['page_type']
        if 'plan_content' in d:
            o.plan_content = d['plan_content']
        if 'plan_source' in d:
            o.plan_source = d['plan_source']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'repeat_times' in d:
            o.repeat_times = d['repeat_times']
        if 'status' in d:
            o.status = d['status']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o


