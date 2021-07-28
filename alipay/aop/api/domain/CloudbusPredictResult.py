#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CloudbusRouteRItem import CloudbusRouteRItem
from alipay.aop.api.domain.CloudbusRouteRItem import CloudbusRouteRItem
from alipay.aop.api.domain.CloudbusRouteRItem import CloudbusRouteRItem


class CloudbusPredictResult(object):

    def __init__(self):
        self._message = None
        self._plan_id = None
        self._progress = None
        self._routes = None
        self._routes_decreased = None
        self._routes_increased = None
        self._status = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        self._progress = value
    @property
    def routes(self):
        return self._routes

    @routes.setter
    def routes(self, value):
        if isinstance(value, list):
            self._routes = list()
            for i in value:
                if isinstance(i, CloudbusRouteRItem):
                    self._routes.append(i)
                else:
                    self._routes.append(CloudbusRouteRItem.from_alipay_dict(i))
    @property
    def routes_decreased(self):
        return self._routes_decreased

    @routes_decreased.setter
    def routes_decreased(self, value):
        if isinstance(value, list):
            self._routes_decreased = list()
            for i in value:
                if isinstance(i, CloudbusRouteRItem):
                    self._routes_decreased.append(i)
                else:
                    self._routes_decreased.append(CloudbusRouteRItem.from_alipay_dict(i))
    @property
    def routes_increased(self):
        return self._routes_increased

    @routes_increased.setter
    def routes_increased(self, value):
        if isinstance(value, list):
            self._routes_increased = list()
            for i in value:
                if isinstance(i, CloudbusRouteRItem):
                    self._routes_increased.append(i)
                else:
                    self._routes_increased.append(CloudbusRouteRItem.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.progress:
            if hasattr(self.progress, 'to_alipay_dict'):
                params['progress'] = self.progress.to_alipay_dict()
            else:
                params['progress'] = self.progress
        if self.routes:
            if isinstance(self.routes, list):
                for i in range(0, len(self.routes)):
                    element = self.routes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.routes[i] = element.to_alipay_dict()
            if hasattr(self.routes, 'to_alipay_dict'):
                params['routes'] = self.routes.to_alipay_dict()
            else:
                params['routes'] = self.routes
        if self.routes_decreased:
            if isinstance(self.routes_decreased, list):
                for i in range(0, len(self.routes_decreased)):
                    element = self.routes_decreased[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.routes_decreased[i] = element.to_alipay_dict()
            if hasattr(self.routes_decreased, 'to_alipay_dict'):
                params['routes_decreased'] = self.routes_decreased.to_alipay_dict()
            else:
                params['routes_decreased'] = self.routes_decreased
        if self.routes_increased:
            if isinstance(self.routes_increased, list):
                for i in range(0, len(self.routes_increased)):
                    element = self.routes_increased[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.routes_increased[i] = element.to_alipay_dict()
            if hasattr(self.routes_increased, 'to_alipay_dict'):
                params['routes_increased'] = self.routes_increased.to_alipay_dict()
            else:
                params['routes_increased'] = self.routes_increased
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudbusPredictResult()
        if 'message' in d:
            o.message = d['message']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'progress' in d:
            o.progress = d['progress']
        if 'routes' in d:
            o.routes = d['routes']
        if 'routes_decreased' in d:
            o.routes_decreased = d['routes_decreased']
        if 'routes_increased' in d:
            o.routes_increased = d['routes_increased']
        if 'status' in d:
            o.status = d['status']
        return o


