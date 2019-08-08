# from pyramid.config import Configurator
# from pyramid.events import ApplicationCreated
# from pyramid_watcher.subscribers import start_changesethandler
#
# from .subscribers import start_threadrunner, ChangesetHandler
# from .views import livereload_view
#
#
# def includeme(config: Configurator):
#     # The ChangesetHandler is a persistent callable which
#     # accepts changesets, stores them, and broadcasts an
#     # event. It is stored in a well-known place in the registry.
#     config.add_subscriber(start_changesethandler, ApplicationCreated)
#
#     # SSE: livreload view, static view for the JS asset
#     config.add_route('livereload', '/livereload')
#     config.add_view(route_name='livereload', view=livereload_view)
#     config.add_static_view(
#         name='watcher_static',
#         path='pyramid_watcher:static'
#     )
#
#     # The Threadrunner watches changes on disk and calls the callback.
#     # Subscribe to ApplicationCreated to start the
#     # threadrunner as late as possible
#     config.add_subscriber(start_threadrunner, ApplicationCreated)
#
