#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CallDetailDTO(object):

    def __init__(self):
        self._additional_broker = None
        self._agent_ids = None
        self._agent_names = None
        self._broker = None
        self._call_duration = None
        self._called_number = None
        self._callee_location = None
        self._caller_location = None
        self._calling_number = None
        self._contact_disposition = None
        self._contact_id = None
        self._contact_type = None
        self._early_media_state = None
        self._established_time = None
        self._instance_id = None
        self._ivr_time = None
        self._queue_time = None
        self._recording_duration = None
        self._recording_ready = None
        self._release_initiator = None
        self._release_time = None
        self._ring_time = None
        self._satisfaction_description = None
        self._satisfaction_index = None
        self._satisfaction_survey_channel = None
        self._satisfaction_survey_offered = None
        self._skill_group_ids = None
        self._skill_group_names = None
        self._start_time = None
        self._wait_time = None

    @property
    def additional_broker(self):
        return self._additional_broker

    @additional_broker.setter
    def additional_broker(self, value):
        self._additional_broker = value
    @property
    def agent_ids(self):
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, value):
        if isinstance(value, list):
            self._agent_ids = list()
            for i in value:
                self._agent_ids.append(i)
    @property
    def agent_names(self):
        return self._agent_names

    @agent_names.setter
    def agent_names(self, value):
        if isinstance(value, list):
            self._agent_names = list()
            for i in value:
                self._agent_names.append(i)
    @property
    def broker(self):
        return self._broker

    @broker.setter
    def broker(self, value):
        self._broker = value
    @property
    def call_duration(self):
        return self._call_duration

    @call_duration.setter
    def call_duration(self, value):
        self._call_duration = value
    @property
    def called_number(self):
        return self._called_number

    @called_number.setter
    def called_number(self, value):
        self._called_number = value
    @property
    def callee_location(self):
        return self._callee_location

    @callee_location.setter
    def callee_location(self, value):
        self._callee_location = value
    @property
    def caller_location(self):
        return self._caller_location

    @caller_location.setter
    def caller_location(self, value):
        self._caller_location = value
    @property
    def calling_number(self):
        return self._calling_number

    @calling_number.setter
    def calling_number(self, value):
        self._calling_number = value
    @property
    def contact_disposition(self):
        return self._contact_disposition

    @contact_disposition.setter
    def contact_disposition(self, value):
        self._contact_disposition = value
    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, value):
        self._contact_id = value
    @property
    def contact_type(self):
        return self._contact_type

    @contact_type.setter
    def contact_type(self, value):
        self._contact_type = value
    @property
    def early_media_state(self):
        return self._early_media_state

    @early_media_state.setter
    def early_media_state(self, value):
        self._early_media_state = value
    @property
    def established_time(self):
        return self._established_time

    @established_time.setter
    def established_time(self, value):
        self._established_time = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def ivr_time(self):
        return self._ivr_time

    @ivr_time.setter
    def ivr_time(self, value):
        self._ivr_time = value
    @property
    def queue_time(self):
        return self._queue_time

    @queue_time.setter
    def queue_time(self, value):
        self._queue_time = value
    @property
    def recording_duration(self):
        return self._recording_duration

    @recording_duration.setter
    def recording_duration(self, value):
        self._recording_duration = value
    @property
    def recording_ready(self):
        return self._recording_ready

    @recording_ready.setter
    def recording_ready(self, value):
        self._recording_ready = value
    @property
    def release_initiator(self):
        return self._release_initiator

    @release_initiator.setter
    def release_initiator(self, value):
        self._release_initiator = value
    @property
    def release_time(self):
        return self._release_time

    @release_time.setter
    def release_time(self, value):
        self._release_time = value
    @property
    def ring_time(self):
        return self._ring_time

    @ring_time.setter
    def ring_time(self, value):
        self._ring_time = value
    @property
    def satisfaction_description(self):
        return self._satisfaction_description

    @satisfaction_description.setter
    def satisfaction_description(self, value):
        self._satisfaction_description = value
    @property
    def satisfaction_index(self):
        return self._satisfaction_index

    @satisfaction_index.setter
    def satisfaction_index(self, value):
        self._satisfaction_index = value
    @property
    def satisfaction_survey_channel(self):
        return self._satisfaction_survey_channel

    @satisfaction_survey_channel.setter
    def satisfaction_survey_channel(self, value):
        self._satisfaction_survey_channel = value
    @property
    def satisfaction_survey_offered(self):
        return self._satisfaction_survey_offered

    @satisfaction_survey_offered.setter
    def satisfaction_survey_offered(self, value):
        self._satisfaction_survey_offered = value
    @property
    def skill_group_ids(self):
        return self._skill_group_ids

    @skill_group_ids.setter
    def skill_group_ids(self, value):
        if isinstance(value, list):
            self._skill_group_ids = list()
            for i in value:
                self._skill_group_ids.append(i)
    @property
    def skill_group_names(self):
        return self._skill_group_names

    @skill_group_names.setter
    def skill_group_names(self, value):
        if isinstance(value, list):
            self._skill_group_names = list()
            for i in value:
                self._skill_group_names.append(i)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def wait_time(self):
        return self._wait_time

    @wait_time.setter
    def wait_time(self, value):
        self._wait_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_broker:
            if hasattr(self.additional_broker, 'to_alipay_dict'):
                params['additional_broker'] = self.additional_broker.to_alipay_dict()
            else:
                params['additional_broker'] = self.additional_broker
        if self.agent_ids:
            if isinstance(self.agent_ids, list):
                for i in range(0, len(self.agent_ids)):
                    element = self.agent_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agent_ids[i] = element.to_alipay_dict()
            if hasattr(self.agent_ids, 'to_alipay_dict'):
                params['agent_ids'] = self.agent_ids.to_alipay_dict()
            else:
                params['agent_ids'] = self.agent_ids
        if self.agent_names:
            if isinstance(self.agent_names, list):
                for i in range(0, len(self.agent_names)):
                    element = self.agent_names[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agent_names[i] = element.to_alipay_dict()
            if hasattr(self.agent_names, 'to_alipay_dict'):
                params['agent_names'] = self.agent_names.to_alipay_dict()
            else:
                params['agent_names'] = self.agent_names
        if self.broker:
            if hasattr(self.broker, 'to_alipay_dict'):
                params['broker'] = self.broker.to_alipay_dict()
            else:
                params['broker'] = self.broker
        if self.call_duration:
            if hasattr(self.call_duration, 'to_alipay_dict'):
                params['call_duration'] = self.call_duration.to_alipay_dict()
            else:
                params['call_duration'] = self.call_duration
        if self.called_number:
            if hasattr(self.called_number, 'to_alipay_dict'):
                params['called_number'] = self.called_number.to_alipay_dict()
            else:
                params['called_number'] = self.called_number
        if self.callee_location:
            if hasattr(self.callee_location, 'to_alipay_dict'):
                params['callee_location'] = self.callee_location.to_alipay_dict()
            else:
                params['callee_location'] = self.callee_location
        if self.caller_location:
            if hasattr(self.caller_location, 'to_alipay_dict'):
                params['caller_location'] = self.caller_location.to_alipay_dict()
            else:
                params['caller_location'] = self.caller_location
        if self.calling_number:
            if hasattr(self.calling_number, 'to_alipay_dict'):
                params['calling_number'] = self.calling_number.to_alipay_dict()
            else:
                params['calling_number'] = self.calling_number
        if self.contact_disposition:
            if hasattr(self.contact_disposition, 'to_alipay_dict'):
                params['contact_disposition'] = self.contact_disposition.to_alipay_dict()
            else:
                params['contact_disposition'] = self.contact_disposition
        if self.contact_id:
            if hasattr(self.contact_id, 'to_alipay_dict'):
                params['contact_id'] = self.contact_id.to_alipay_dict()
            else:
                params['contact_id'] = self.contact_id
        if self.contact_type:
            if hasattr(self.contact_type, 'to_alipay_dict'):
                params['contact_type'] = self.contact_type.to_alipay_dict()
            else:
                params['contact_type'] = self.contact_type
        if self.early_media_state:
            if hasattr(self.early_media_state, 'to_alipay_dict'):
                params['early_media_state'] = self.early_media_state.to_alipay_dict()
            else:
                params['early_media_state'] = self.early_media_state
        if self.established_time:
            if hasattr(self.established_time, 'to_alipay_dict'):
                params['established_time'] = self.established_time.to_alipay_dict()
            else:
                params['established_time'] = self.established_time
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.ivr_time:
            if hasattr(self.ivr_time, 'to_alipay_dict'):
                params['ivr_time'] = self.ivr_time.to_alipay_dict()
            else:
                params['ivr_time'] = self.ivr_time
        if self.queue_time:
            if hasattr(self.queue_time, 'to_alipay_dict'):
                params['queue_time'] = self.queue_time.to_alipay_dict()
            else:
                params['queue_time'] = self.queue_time
        if self.recording_duration:
            if hasattr(self.recording_duration, 'to_alipay_dict'):
                params['recording_duration'] = self.recording_duration.to_alipay_dict()
            else:
                params['recording_duration'] = self.recording_duration
        if self.recording_ready:
            if hasattr(self.recording_ready, 'to_alipay_dict'):
                params['recording_ready'] = self.recording_ready.to_alipay_dict()
            else:
                params['recording_ready'] = self.recording_ready
        if self.release_initiator:
            if hasattr(self.release_initiator, 'to_alipay_dict'):
                params['release_initiator'] = self.release_initiator.to_alipay_dict()
            else:
                params['release_initiator'] = self.release_initiator
        if self.release_time:
            if hasattr(self.release_time, 'to_alipay_dict'):
                params['release_time'] = self.release_time.to_alipay_dict()
            else:
                params['release_time'] = self.release_time
        if self.ring_time:
            if hasattr(self.ring_time, 'to_alipay_dict'):
                params['ring_time'] = self.ring_time.to_alipay_dict()
            else:
                params['ring_time'] = self.ring_time
        if self.satisfaction_description:
            if hasattr(self.satisfaction_description, 'to_alipay_dict'):
                params['satisfaction_description'] = self.satisfaction_description.to_alipay_dict()
            else:
                params['satisfaction_description'] = self.satisfaction_description
        if self.satisfaction_index:
            if hasattr(self.satisfaction_index, 'to_alipay_dict'):
                params['satisfaction_index'] = self.satisfaction_index.to_alipay_dict()
            else:
                params['satisfaction_index'] = self.satisfaction_index
        if self.satisfaction_survey_channel:
            if hasattr(self.satisfaction_survey_channel, 'to_alipay_dict'):
                params['satisfaction_survey_channel'] = self.satisfaction_survey_channel.to_alipay_dict()
            else:
                params['satisfaction_survey_channel'] = self.satisfaction_survey_channel
        if self.satisfaction_survey_offered:
            if hasattr(self.satisfaction_survey_offered, 'to_alipay_dict'):
                params['satisfaction_survey_offered'] = self.satisfaction_survey_offered.to_alipay_dict()
            else:
                params['satisfaction_survey_offered'] = self.satisfaction_survey_offered
        if self.skill_group_ids:
            if isinstance(self.skill_group_ids, list):
                for i in range(0, len(self.skill_group_ids)):
                    element = self.skill_group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skill_group_ids[i] = element.to_alipay_dict()
            if hasattr(self.skill_group_ids, 'to_alipay_dict'):
                params['skill_group_ids'] = self.skill_group_ids.to_alipay_dict()
            else:
                params['skill_group_ids'] = self.skill_group_ids
        if self.skill_group_names:
            if isinstance(self.skill_group_names, list):
                for i in range(0, len(self.skill_group_names)):
                    element = self.skill_group_names[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skill_group_names[i] = element.to_alipay_dict()
            if hasattr(self.skill_group_names, 'to_alipay_dict'):
                params['skill_group_names'] = self.skill_group_names.to_alipay_dict()
            else:
                params['skill_group_names'] = self.skill_group_names
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.wait_time:
            if hasattr(self.wait_time, 'to_alipay_dict'):
                params['wait_time'] = self.wait_time.to_alipay_dict()
            else:
                params['wait_time'] = self.wait_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CallDetailDTO()
        if 'additional_broker' in d:
            o.additional_broker = d['additional_broker']
        if 'agent_ids' in d:
            o.agent_ids = d['agent_ids']
        if 'agent_names' in d:
            o.agent_names = d['agent_names']
        if 'broker' in d:
            o.broker = d['broker']
        if 'call_duration' in d:
            o.call_duration = d['call_duration']
        if 'called_number' in d:
            o.called_number = d['called_number']
        if 'callee_location' in d:
            o.callee_location = d['callee_location']
        if 'caller_location' in d:
            o.caller_location = d['caller_location']
        if 'calling_number' in d:
            o.calling_number = d['calling_number']
        if 'contact_disposition' in d:
            o.contact_disposition = d['contact_disposition']
        if 'contact_id' in d:
            o.contact_id = d['contact_id']
        if 'contact_type' in d:
            o.contact_type = d['contact_type']
        if 'early_media_state' in d:
            o.early_media_state = d['early_media_state']
        if 'established_time' in d:
            o.established_time = d['established_time']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'ivr_time' in d:
            o.ivr_time = d['ivr_time']
        if 'queue_time' in d:
            o.queue_time = d['queue_time']
        if 'recording_duration' in d:
            o.recording_duration = d['recording_duration']
        if 'recording_ready' in d:
            o.recording_ready = d['recording_ready']
        if 'release_initiator' in d:
            o.release_initiator = d['release_initiator']
        if 'release_time' in d:
            o.release_time = d['release_time']
        if 'ring_time' in d:
            o.ring_time = d['ring_time']
        if 'satisfaction_description' in d:
            o.satisfaction_description = d['satisfaction_description']
        if 'satisfaction_index' in d:
            o.satisfaction_index = d['satisfaction_index']
        if 'satisfaction_survey_channel' in d:
            o.satisfaction_survey_channel = d['satisfaction_survey_channel']
        if 'satisfaction_survey_offered' in d:
            o.satisfaction_survey_offered = d['satisfaction_survey_offered']
        if 'skill_group_ids' in d:
            o.skill_group_ids = d['skill_group_ids']
        if 'skill_group_names' in d:
            o.skill_group_names = d['skill_group_names']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'wait_time' in d:
            o.wait_time = d['wait_time']
        return o


