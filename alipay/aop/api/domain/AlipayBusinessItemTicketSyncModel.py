#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicExtInfo import ScenicExtInfo


class AlipayBusinessItemTicketSyncModel(object):

    def __init__(self):
        self._ext_info = None
        self._name = None
        self._outer_scenic_id = None
        self._outer_ticket_id = None
        self._partner_id = None
        self._pic = None
        self._scenic_app_id = None
        self._source_system = None
        self._status = None
        self._ticket_goods_id = None
        self._ticket_link = None
        self._ticket_modified_time = None
        self._ticket_specs = None
        self._ticket_type = None
        self._update_msg = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ScenicExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ScenicExtInfo.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def outer_scenic_id(self):
        return self._outer_scenic_id

    @outer_scenic_id.setter
    def outer_scenic_id(self, value):
        self._outer_scenic_id = value
    @property
    def outer_ticket_id(self):
        return self._outer_ticket_id

    @outer_ticket_id.setter
    def outer_ticket_id(self, value):
        self._outer_ticket_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pic(self):
        return self._pic

    @pic.setter
    def pic(self, value):
        self._pic = value
    @property
    def scenic_app_id(self):
        return self._scenic_app_id

    @scenic_app_id.setter
    def scenic_app_id(self, value):
        self._scenic_app_id = value
    @property
    def source_system(self):
        return self._source_system

    @source_system.setter
    def source_system(self, value):
        self._source_system = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def ticket_goods_id(self):
        return self._ticket_goods_id

    @ticket_goods_id.setter
    def ticket_goods_id(self, value):
        self._ticket_goods_id = value
    @property
    def ticket_link(self):
        return self._ticket_link

    @ticket_link.setter
    def ticket_link(self, value):
        self._ticket_link = value
    @property
    def ticket_modified_time(self):
        return self._ticket_modified_time

    @ticket_modified_time.setter
    def ticket_modified_time(self, value):
        self._ticket_modified_time = value
    @property
    def ticket_specs(self):
        return self._ticket_specs

    @ticket_specs.setter
    def ticket_specs(self, value):
        if isinstance(value, list):
            self._ticket_specs = list()
            for i in value:
                self._ticket_specs.append(i)
    @property
    def ticket_type(self):
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, value):
        self._ticket_type = value
    @property
    def update_msg(self):
        return self._update_msg

    @update_msg.setter
    def update_msg(self, value):
        self._update_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.outer_scenic_id:
            if hasattr(self.outer_scenic_id, 'to_alipay_dict'):
                params['outer_scenic_id'] = self.outer_scenic_id.to_alipay_dict()
            else:
                params['outer_scenic_id'] = self.outer_scenic_id
        if self.outer_ticket_id:
            if hasattr(self.outer_ticket_id, 'to_alipay_dict'):
                params['outer_ticket_id'] = self.outer_ticket_id.to_alipay_dict()
            else:
                params['outer_ticket_id'] = self.outer_ticket_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pic:
            if hasattr(self.pic, 'to_alipay_dict'):
                params['pic'] = self.pic.to_alipay_dict()
            else:
                params['pic'] = self.pic
        if self.scenic_app_id:
            if hasattr(self.scenic_app_id, 'to_alipay_dict'):
                params['scenic_app_id'] = self.scenic_app_id.to_alipay_dict()
            else:
                params['scenic_app_id'] = self.scenic_app_id
        if self.source_system:
            if hasattr(self.source_system, 'to_alipay_dict'):
                params['source_system'] = self.source_system.to_alipay_dict()
            else:
                params['source_system'] = self.source_system
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.ticket_goods_id:
            if hasattr(self.ticket_goods_id, 'to_alipay_dict'):
                params['ticket_goods_id'] = self.ticket_goods_id.to_alipay_dict()
            else:
                params['ticket_goods_id'] = self.ticket_goods_id
        if self.ticket_link:
            if hasattr(self.ticket_link, 'to_alipay_dict'):
                params['ticket_link'] = self.ticket_link.to_alipay_dict()
            else:
                params['ticket_link'] = self.ticket_link
        if self.ticket_modified_time:
            if hasattr(self.ticket_modified_time, 'to_alipay_dict'):
                params['ticket_modified_time'] = self.ticket_modified_time.to_alipay_dict()
            else:
                params['ticket_modified_time'] = self.ticket_modified_time
        if self.ticket_specs:
            if isinstance(self.ticket_specs, list):
                for i in range(0, len(self.ticket_specs)):
                    element = self.ticket_specs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ticket_specs[i] = element.to_alipay_dict()
            if hasattr(self.ticket_specs, 'to_alipay_dict'):
                params['ticket_specs'] = self.ticket_specs.to_alipay_dict()
            else:
                params['ticket_specs'] = self.ticket_specs
        if self.ticket_type:
            if hasattr(self.ticket_type, 'to_alipay_dict'):
                params['ticket_type'] = self.ticket_type.to_alipay_dict()
            else:
                params['ticket_type'] = self.ticket_type
        if self.update_msg:
            if hasattr(self.update_msg, 'to_alipay_dict'):
                params['update_msg'] = self.update_msg.to_alipay_dict()
            else:
                params['update_msg'] = self.update_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessItemTicketSyncModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'name' in d:
            o.name = d['name']
        if 'outer_scenic_id' in d:
            o.outer_scenic_id = d['outer_scenic_id']
        if 'outer_ticket_id' in d:
            o.outer_ticket_id = d['outer_ticket_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pic' in d:
            o.pic = d['pic']
        if 'scenic_app_id' in d:
            o.scenic_app_id = d['scenic_app_id']
        if 'source_system' in d:
            o.source_system = d['source_system']
        if 'status' in d:
            o.status = d['status']
        if 'ticket_goods_id' in d:
            o.ticket_goods_id = d['ticket_goods_id']
        if 'ticket_link' in d:
            o.ticket_link = d['ticket_link']
        if 'ticket_modified_time' in d:
            o.ticket_modified_time = d['ticket_modified_time']
        if 'ticket_specs' in d:
            o.ticket_specs = d['ticket_specs']
        if 'ticket_type' in d:
            o.ticket_type = d['ticket_type']
        if 'update_msg' in d:
            o.update_msg = d['update_msg']
        return o


