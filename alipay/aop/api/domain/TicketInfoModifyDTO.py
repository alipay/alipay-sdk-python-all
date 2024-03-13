#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TicketInfoModifyDTO(object):

    def __init__(self):
        self._event_end_time = None
        self._event_id = None
        self._event_start_time = None
        self._event_status = None
        self._performance_seats = None
        self._ticket_id = None
        self._ticket_link = None
        self._ticket_status = None

    @property
    def event_end_time(self):
        return self._event_end_time

    @event_end_time.setter
    def event_end_time(self, value):
        self._event_end_time = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def event_start_time(self):
        return self._event_start_time

    @event_start_time.setter
    def event_start_time(self, value):
        self._event_start_time = value
    @property
    def event_status(self):
        return self._event_status

    @event_status.setter
    def event_status(self, value):
        self._event_status = value
    @property
    def performance_seats(self):
        return self._performance_seats

    @performance_seats.setter
    def performance_seats(self, value):
        self._performance_seats = value
    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        self._ticket_id = value
    @property
    def ticket_link(self):
        return self._ticket_link

    @ticket_link.setter
    def ticket_link(self, value):
        self._ticket_link = value
    @property
    def ticket_status(self):
        return self._ticket_status

    @ticket_status.setter
    def ticket_status(self, value):
        self._ticket_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_end_time:
            if hasattr(self.event_end_time, 'to_alipay_dict'):
                params['event_end_time'] = self.event_end_time.to_alipay_dict()
            else:
                params['event_end_time'] = self.event_end_time
        if self.event_id:
            if hasattr(self.event_id, 'to_alipay_dict'):
                params['event_id'] = self.event_id.to_alipay_dict()
            else:
                params['event_id'] = self.event_id
        if self.event_start_time:
            if hasattr(self.event_start_time, 'to_alipay_dict'):
                params['event_start_time'] = self.event_start_time.to_alipay_dict()
            else:
                params['event_start_time'] = self.event_start_time
        if self.event_status:
            if hasattr(self.event_status, 'to_alipay_dict'):
                params['event_status'] = self.event_status.to_alipay_dict()
            else:
                params['event_status'] = self.event_status
        if self.performance_seats:
            if hasattr(self.performance_seats, 'to_alipay_dict'):
                params['performance_seats'] = self.performance_seats.to_alipay_dict()
            else:
                params['performance_seats'] = self.performance_seats
        if self.ticket_id:
            if hasattr(self.ticket_id, 'to_alipay_dict'):
                params['ticket_id'] = self.ticket_id.to_alipay_dict()
            else:
                params['ticket_id'] = self.ticket_id
        if self.ticket_link:
            if hasattr(self.ticket_link, 'to_alipay_dict'):
                params['ticket_link'] = self.ticket_link.to_alipay_dict()
            else:
                params['ticket_link'] = self.ticket_link
        if self.ticket_status:
            if hasattr(self.ticket_status, 'to_alipay_dict'):
                params['ticket_status'] = self.ticket_status.to_alipay_dict()
            else:
                params['ticket_status'] = self.ticket_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TicketInfoModifyDTO()
        if 'event_end_time' in d:
            o.event_end_time = d['event_end_time']
        if 'event_id' in d:
            o.event_id = d['event_id']
        if 'event_start_time' in d:
            o.event_start_time = d['event_start_time']
        if 'event_status' in d:
            o.event_status = d['event_status']
        if 'performance_seats' in d:
            o.performance_seats = d['performance_seats']
        if 'ticket_id' in d:
            o.ticket_id = d['ticket_id']
        if 'ticket_link' in d:
            o.ticket_link = d['ticket_link']
        if 'ticket_status' in d:
            o.ticket_status = d['ticket_status']
        return o


