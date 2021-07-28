#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardInstanceDO import CardInstanceDO
from alipay.aop.api.domain.CardPromoDO import CardPromoDO


class QuestInstanceDO(object):

    def __init__(self):
        self._action_schema = None
        self._card_instance = None
        self._card_promos = None
        self._day_count = None
        self._icon = None
        self._instance_id = None
        self._join_count = None
        self._joined = None
        self._marked = None
        self._quest_id = None
        self._remind_times = None
        self._title = None

    @property
    def action_schema(self):
        return self._action_schema

    @action_schema.setter
    def action_schema(self, value):
        self._action_schema = value
    @property
    def card_instance(self):
        return self._card_instance

    @card_instance.setter
    def card_instance(self, value):
        if isinstance(value, CardInstanceDO):
            self._card_instance = value
        else:
            self._card_instance = CardInstanceDO.from_alipay_dict(value)
    @property
    def card_promos(self):
        return self._card_promos

    @card_promos.setter
    def card_promos(self, value):
        if isinstance(value, list):
            self._card_promos = list()
            for i in value:
                if isinstance(i, CardPromoDO):
                    self._card_promos.append(i)
                else:
                    self._card_promos.append(CardPromoDO.from_alipay_dict(i))
    @property
    def day_count(self):
        return self._day_count

    @day_count.setter
    def day_count(self, value):
        self._day_count = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def join_count(self):
        return self._join_count

    @join_count.setter
    def join_count(self, value):
        self._join_count = value
    @property
    def joined(self):
        return self._joined

    @joined.setter
    def joined(self, value):
        self._joined = value
    @property
    def marked(self):
        return self._marked

    @marked.setter
    def marked(self, value):
        self._marked = value
    @property
    def quest_id(self):
        return self._quest_id

    @quest_id.setter
    def quest_id(self, value):
        self._quest_id = value
    @property
    def remind_times(self):
        return self._remind_times

    @remind_times.setter
    def remind_times(self, value):
        if isinstance(value, list):
            self._remind_times = list()
            for i in value:
                self._remind_times.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_schema:
            if hasattr(self.action_schema, 'to_alipay_dict'):
                params['action_schema'] = self.action_schema.to_alipay_dict()
            else:
                params['action_schema'] = self.action_schema
        if self.card_instance:
            if hasattr(self.card_instance, 'to_alipay_dict'):
                params['card_instance'] = self.card_instance.to_alipay_dict()
            else:
                params['card_instance'] = self.card_instance
        if self.card_promos:
            if isinstance(self.card_promos, list):
                for i in range(0, len(self.card_promos)):
                    element = self.card_promos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_promos[i] = element.to_alipay_dict()
            if hasattr(self.card_promos, 'to_alipay_dict'):
                params['card_promos'] = self.card_promos.to_alipay_dict()
            else:
                params['card_promos'] = self.card_promos
        if self.day_count:
            if hasattr(self.day_count, 'to_alipay_dict'):
                params['day_count'] = self.day_count.to_alipay_dict()
            else:
                params['day_count'] = self.day_count
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.join_count:
            if hasattr(self.join_count, 'to_alipay_dict'):
                params['join_count'] = self.join_count.to_alipay_dict()
            else:
                params['join_count'] = self.join_count
        if self.joined:
            if hasattr(self.joined, 'to_alipay_dict'):
                params['joined'] = self.joined.to_alipay_dict()
            else:
                params['joined'] = self.joined
        if self.marked:
            if hasattr(self.marked, 'to_alipay_dict'):
                params['marked'] = self.marked.to_alipay_dict()
            else:
                params['marked'] = self.marked
        if self.quest_id:
            if hasattr(self.quest_id, 'to_alipay_dict'):
                params['quest_id'] = self.quest_id.to_alipay_dict()
            else:
                params['quest_id'] = self.quest_id
        if self.remind_times:
            if isinstance(self.remind_times, list):
                for i in range(0, len(self.remind_times)):
                    element = self.remind_times[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.remind_times[i] = element.to_alipay_dict()
            if hasattr(self.remind_times, 'to_alipay_dict'):
                params['remind_times'] = self.remind_times.to_alipay_dict()
            else:
                params['remind_times'] = self.remind_times
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QuestInstanceDO()
        if 'action_schema' in d:
            o.action_schema = d['action_schema']
        if 'card_instance' in d:
            o.card_instance = d['card_instance']
        if 'card_promos' in d:
            o.card_promos = d['card_promos']
        if 'day_count' in d:
            o.day_count = d['day_count']
        if 'icon' in d:
            o.icon = d['icon']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'join_count' in d:
            o.join_count = d['join_count']
        if 'joined' in d:
            o.joined = d['joined']
        if 'marked' in d:
            o.marked = d['marked']
        if 'quest_id' in d:
            o.quest_id = d['quest_id']
        if 'remind_times' in d:
            o.remind_times = d['remind_times']
        if 'title' in d:
            o.title = d['title']
        return o


