Research for sprint with Jim Fulton
===================================

In September 2019, before PyColorado, I'm sprinting with Jim to learn
some patterns about ZODB, pseudo-reactive programming, generational
sets, references, high performance collections, etc.

Here are some things to ask Jim about.

pydantic
========

- Can't use with Persistent::

    File "/Users/pauleveritt/projects/pauleveritt/kaybee/jimfulton_research/.venv/lib/python3.7/site-packages/pydantic/dataclasses.py", line 73, in _pydantic_post_init
        object.__setattr__(self, '__dict__', d)
    TypeError: can't apply this __setattr__ to persistent.Persistent object

- Based on this, revisit the idea of persisting general dataclasses, not
  subclassed from persistent, via immer-style "here's a copy with a proxy,
  scribble on it, hand it back, and I'll persist it" in a "store"

    - From `Writing Persistent Objects <http://www.zodb.org/en/latest/guide/writing-persistent-objects.html>`_::

        Because tuples are immutable, they satisfy the rules of persistence
        without any special handling.



Generations
===========

- Impact of code changes, not data changes, and caching intermediate
  representations (e.g. rendered components, image variations)

  - How to detect thumbnail.py or breadcrumbs.py changed

  - Do these code artifacts get considered as part of the generation?

- What if it is a rebuild of the universe and there are 10,000 adds? Is
  “contents” support enough?

- How are deletes tracked?

- Should this extend to instances of a component on a page, and even all
  the variations (e.g. batches) of that component instance?

General ZODB
============

- Scripts to pack

General Python
==============

- Circular import avoidance and ``__all__``
