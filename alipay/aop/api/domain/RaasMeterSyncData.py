#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RaasMeterSyncData(object):

    def __init__(self):
        self._aggregate_term = None
        self._aggregate_value = None
        self._amount_term = None
        self._biz_type = None
        self._channel = None
        self._count = None
        self._data_id = None
        self._gmt_end_time = None
        self._gmt_start_time = None
        self._meter_domain = None
        self._product_code = None
        self._site = None
        self._status = None
        self._tenant = None
        self._time_partition = None
        self._time_zone = None

    @property
    def aggregate_term(self):
        return self._aggregate_term

    @aggregate_term.setter
    def aggregate_term(self, value):
        self._aggregate_term = value
    @property
    def aggregate_value(self):
        return self._aggregate_value

    @aggregate_value.setter
    def aggregate_value(self, value):
        self._aggregate_value = value
    @property
    def amount_term(self):
        return self._amount_term

    @amount_term.setter
    def amount_term(self, value):
        self._amount_term = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def gmt_end_time(self):
        return self._gmt_end_time

    @gmt_end_time.setter
    def gmt_end_time(self, value):
        self._gmt_end_time = value
    @property
    def gmt_start_time(self):
        return self._gmt_start_time

    @gmt_start_time.setter
    def gmt_start_time(self, value):
        self._gmt_start_time = value
    @property
    def meter_domain(self):
        return self._meter_domain

    @meter_domain.setter
    def meter_domain(self, value):
        self._meter_domain = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def time_partition(self):
        return self._time_partition

    @time_partition.setter
    def time_partition(self, value):
        self._time_partition = value
    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        self._time_zone = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggregate_term:
            if hasattr(self.aggregate_term, 'to_alipay_dict'):
                params['aggregate_term'] = self.aggregate_term.to_alipay_dict()
            else:
                params['aggregate_term'] = self.aggregate_term
        if self.aggregate_value:
            if hasattr(self.aggregate_value, 'to_alipay_dict'):
                params['aggregate_value'] = self.aggregate_value.to_alipay_dict()
            else:
                params['aggregate_value'] = self.aggregate_value
        if self.amount_term:
            if hasattr(self.amount_term, 'to_alipay_dict'):
                params['amount_term'] = self.amount_term.to_alipay_dict()
            else:
                params['amount_term'] = self.amount_term
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.gmt_end_time:
            if hasattr(self.gmt_end_time, 'to_alipay_dict'):
                params['gmt_end_time'] = self.gmt_end_time.to_alipay_dict()
            else:
                params['gmt_end_time'] = self.gmt_end_time
        if self.gmt_start_time:
            if hasattr(self.gmt_start_time, 'to_alipay_dict'):
                params['gmt_start_time'] = self.gmt_start_time.to_alipay_dict()
            else:
                params['gmt_start_time'] = self.gmt_start_time
        if self.meter_domain:
            if hasattr(self.meter_domain, 'to_alipay_dict'):
                params['meter_domain'] = self.meter_domain.to_alipay_dict()
            else:
                params['meter_domain'] = self.meter_domain
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.time_partition:
            if hasattr(self.time_partition, 'to_alipay_dict'):
                params['time_partition'] = self.time_partition.to_alipay_dict()
            else:
                params['time_partition'] = self.time_partition
        if self.time_zone:
            if hasattr(self.time_zone, 'to_alipay_dict'):
                params['time_zone'] = self.time_zone.to_alipay_dict()
            else:
                params['time_zone'] = self.time_zone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RaasMeterSyncData()
        if 'aggregate_term' in d:
            o.aggregate_term = d['aggregate_term']
        if 'aggregate_value' in d:
            o.aggregate_value = d['aggregate_value']
        if 'amount_term' in d:
            o.amount_term = d['amount_term']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'count' in d:
            o.count = d['count']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'gmt_end_time' in d:
            o.gmt_end_time = d['gmt_end_time']
        if 'gmt_start_time' in d:
            o.gmt_start_time = d['gmt_start_time']
        if 'meter_domain' in d:
            o.meter_domain = d['meter_domain']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'site' in d:
            o.site = d['site']
        if 'status' in d:
            o.status = d['status']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'time_partition' in d:
            o.time_partition = d['time_partition']
        if 'time_zone' in d:
            o.time_zone = d['time_zone']
        return o


